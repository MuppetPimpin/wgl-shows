# casino-bus/: the daily casino bus feed for What's Good Local

One file, `casino-bus/trips.json`: upcoming Good Time Tours casino bus trips to Biloxi from every pickup
(Pensacola, plus Mary Esther, Navarre and Loxley once the "Other pickups" tab is published and its CSV
link is set as `OTHER_CSV_URL` in `build.py`).

## How it updates (no AI, no weekly task)

1. Every morning at 6 AM Central, the "Casino Trips Auto-Update" Apps Script reads the Good Time
   Tours flyer and updates the Casino Trips Google Sheet.
2. At 6:30 AM CST / 7:30 AM CDT, `.github/workflows/casino-bus.yml` runs `casino-bus/build.py`,
   which copies today's and future trips from the sheet into `trips.json` and commits only if
   something changed.

To run it by hand: GitHub → Actions → "Casino bus feed" → Run workflow.

**The weekly scheduled tasks never touch this folder.** Don't hand-edit `trips.json`; fix the sheet
(or the Apps Script) instead and rerun the workflow.

## Readers

Pages load it from
`https://cdn.jsdelivr.net/gh/MuppetPimpin/wgl-shows@main/casino-bus/trips.json`
(or `raw.githubusercontent.com/MuppetPimpin/wgl-shows/main/casino-bus/trips.json` for no CDN cache).

Planned readers: home page "Next casino bus" tile, /guide, WGL-TV, WGL Tab, the WGL app.
The hub page (whatsgoodlocal.com/casino-bus-trips/) and the casino guides read the sheet directly.

## Format

```json
{
  "updated": "YYYY-MM-DD",
  "hub": "https://whatsgoodlocal.com/casino-bus-trips/",
  "reserve_phone": "(850) 476-0046 ext. 0",
  "next": { ...first Pensacola trip in "trips", or null... },
  "pickups": ["Navarre", "Pensacola", ...],
  "trips": [
    {
      "date": "2026-11-12", "day": "Thursday",
      "casino": "Boomtown", "casino_page": "https://whatsgoodlocal.com/casinos/boomtown-casino-biloxi/",
      "departs": "9:00 AM", "start": "2026-11-12T09:00",
      "leave_casino": "4:30 PM", "returns": "6:30 PM",
      "fare": "$30", "free_play": "$20", "free_buffet": true,
      "pickup": "Pensacola",
      "pickup_address": "Good Time Tours, 8084 North Davis Hwy, Pensacola",
      "notes": "..."
    }
  ]
}
```

- `start` is local Central time, `YYYY-MM-DDTHH:MM`. The feed is built once a day, so a reader
  showing "next bus" should skip trips whose `start` has already passed.
- `free_buffet` is true for Thursday/Friday morning trips whose sheet note mentions the buffet.
- One trip per pickup: the same bus day from Mary Esther and Navarre is two entries. Filter by `pickup`.
- Fares differ by pickup ($30 Pensacola and Loxley, $40 Mary Esther and Navarre as of Nov 2026).
- Free play, fares and the buffet offer come from the Good Time Tours flyer and can change.
