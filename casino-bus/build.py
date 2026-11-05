"""Builds casino-bus/trips.json from the published Casino Trips Google Sheet.

Run by .github/workflows/casino-bus.yml every morning. The sheet itself is kept
current by the "Casino Trips Auto-Update" Apps Script, which reads the Good Time
Tours flyer. This script only copies upcoming trips into a feed; it never edits
the sheet.

Usage: python3 casino-bus/build.py            (fetches the sheet)
       python3 casino-bus/build.py file.csv   (reads a local copy)
"""
import csv, io, json, re, sys, urllib.request
from datetime import datetime, timedelta, timezone

CSV_URL = ("https://docs.google.com/spreadsheets/d/e/"
           "2PACX-1vQnYBtC2oWBJEZlAqrcWWJgkWxjNxfe1w337KqXps_Qa58RhUNV3LRUVAXjDqyuCyeIB7khsQsxRrVs"
           "/pub?gid=0&single=true&output=csv")
# The "Other pickups" tab (Mary Esther, Navarre, Loxley). Leave "" until that tab is published.
OTHER_CSV_URL = ("https://docs.google.com/spreadsheets/d/e/"
                 "2PACX-1vQnYBtC2oWBJEZlAqrcWWJgkWxjNxfe1w337KqXps_Qa58RhUNV3LRUVAXjDqyuCyeIB7khsQsxRrVs"
                 "/pub?gid=867986559&single=true&output=csv")
OUT = "casino-bus/trips.json"
PICKUP_ADDRESS = {"pensacola": "Good Time Tours, 8084 North Davis Hwy, Pensacola"}
HUB = "https://whatsgoodlocal.com/casino-bus-trips/"
CASINOS = {
    "ip casino":   ("IP Casino",   "https://whatsgoodlocal.com/casinos/ip-casino-biloxi/"),
    "boomtown":    ("Boomtown",    "https://whatsgoodlocal.com/casinos/boomtown-casino-biloxi/"),
    "beau rivage": ("Beau Rivage", "https://whatsgoodlocal.com/casinos/beau-rivage-from-florida/"),
    "hard rock":   ("Hard Rock",   "https://whatsgoodlocal.com/casinos/hard-rock-biloxi/"),
}


def central_today():
    # Central time without a tz database: CDT (UTC-5) Mar-Oct-ish, CST (UTC-6) otherwise.
    now = datetime.now(timezone.utc)
    y = now.year
    def nth_sunday(month, n):
        d = datetime(y, month, 1, tzinfo=timezone.utc)
        d += timedelta(days=(6 - d.weekday()) % 7)
        return d + timedelta(weeks=n - 1)
    dst_start = nth_sunday(3, 2) + timedelta(hours=8)   # 2 AM CST
    dst_end = nth_sunday(11, 1) + timedelta(hours=7)    # 2 AM CDT
    offset = -5 if dst_start <= now < dst_end else -6
    return (now + timedelta(hours=offset)).date().isoformat()


def to24(t):
    m = re.match(r"\s*(\d{1,2}):(\d{2})\s*([AP]M)", t or "", re.I)
    if not m:
        return None
    h = int(m.group(1)) % 12 + (12 if m.group(3).upper() == "PM" else 0)
    return f"{h:02d}:{m.group(2)}"


def main():
    def fetch(url):
        req = urllib.request.Request(url, headers={"User-Agent": "wgl-shows casino-bus feed"})
        return urllib.request.urlopen(req, timeout=60).read().decode("utf-8")

    # Local test: build.py main.csv [other.csv]
    main_text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else fetch(CSV_URL)
    rows = list(csv.DictReader(io.StringIO(main_text)))
    if not rows or "casino" not in rows[0]:
        sys.exit("Sheet came back without a casino column; leaving the feed unchanged.")
    other_text = ""
    if len(sys.argv) > 2:
        other_text = open(sys.argv[2], encoding="utf-8").read()
    elif OTHER_CSV_URL:
        try:
            other_text = fetch(OTHER_CSV_URL)
        except Exception as e:  # the Pensacola feed still builds if this tab is unreachable
            print("Other pickups tab unreachable:", e)
    if other_text:
        other = list(csv.DictReader(io.StringIO(other_text)))
        if other and "casino" in other[0]:
            rows += other

    today = central_today()
    trips = []
    for r in rows:
        r = {k.strip().lower().replace(" ", "_"): (v or "").strip() for k, v in r.items() if k}
        date, casino = r.get("date", ""), r.get("casino", "")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date) or not casino or date < today:
            continue
        dep = to24(r.get("departure_time"))
        if not dep:
            continue
        key = next((k for k in CASINOS if k in casino.lower()), None)
        name, page = CASINOS[key] if key else (casino, HUB)
        notes = r.get("notes", "")
        pickup = r.get("pickup_location", "") or "Pensacola"
        address = r.get("pickup_address", "") or PICKUP_ADDRESS.get(pickup.lower(), "")
        day = r.get("day", "")
        buffet = bool(re.search(r"buffet", notes, re.I)) and day[:3].lower() in ("thu", "fri") \
            and dep < "12:00"
        trips.append({
            "date": date,
            "day": day,
            "casino": name,
            "casino_page": page,
            "departs": r.get("departure_time", ""),
            "start": f"{date}T{dep}",
            "leave_casino": r.get("leave_casino", ""),
            "returns": r.get("return_time", ""),
            "fare": r.get("bus_cost", "") or "$30",
            "free_play": r.get("chips", ""),
            "free_buffet": buffet,
            "pickup": pickup,
            "pickup_address": address,
            "notes": notes,
        })
    trips.sort(key=lambda t: (t["start"], t["pickup"]))

    feed = {
        "_readme": "What's Good Local casino bus feed: upcoming Good Time Tours trips from Pensacola to Biloxi. "
                   "Built every morning by .github/workflows/casino-bus.yml from the Casino Trips sheet (Pensacola tab + Other pickups tab); see casino-bus/CLAUDE.md.",
        "updated": today,
        "hub": HUB,
        "reserve_phone": "(850) 476-0046 ext. 0",
        "next": next((t for t in trips if t["pickup"] == "Pensacola"), None),
        "pickups": sorted({t["pickup"] for t in trips}),
        "trips": trips,
    }
    new = json.dumps(feed, indent=2, ensure_ascii=False) + "\n"
    try:
        old = open(OUT, encoding="utf-8").read()
    except FileNotFoundError:
        old = ""
    if old == new:
        print("No change.")
        return
    open(OUT, "w", encoding="utf-8").write(new)
    print(f"Wrote {len(trips)} upcoming trips (next: {trips[0]['date'] + ' ' + trips[0]['casino'] if trips else 'none'}).")


if __name__ == "__main__":
    main()
