# guide/: the weekly Destin events feed for What's Good Local

One file, `guide/events.json`. It feeds:

| Reader | What it shows |
|---|---|
| The WGL home page guide (whatsgoodlocal.com) | "What's happening" tabs (Tonight / This Weekend / Next 7 Days), category filters, and the Event schema Google reads |
| whatsgoodlocal.com/guide | Same event list, for guests who scan from the hotel TV |

Live music is **not** in this file. The pages pull it from `destin.json` (the live music feed at the
top of this repo) and merge it in as the "Live Music" category. Never touch `destin.json`, the other
city files or `football/` from this job.

## The one rule: no source, no listing

Every event needs a `source`: an https link to the organizer's or venue's own page (city calendar,
venue site, ticket page, official Facebook event) that **states this date** for this event. Aggregator
and "things to do" listicle sites are leads, not sources: open the organizer's page and confirm there.
If the date can't be confirmed, leave the event out. A wrong date is worse than a missing event.

## Window and area

- Run date through **21 days out**. Drop anything whose `end_date` is before the run date.
- Area: Destin, Miramar Beach, Sandestin / Village of Baytowne Wharf, Fort Walton Beach, Okaloosa Island,
  Niceville (Mattie Kelly Arts Center), Santa Rosa Beach / 30A. Seaside and 30A only for bigger events.
- Aim for 25–50 events. Prefer variety across categories and days over many listings from one venue.

## Categories (use exactly these)

`Holiday` · `Comedy` · `Stage` · `Family` · `Tastings` · `Markets`

- Holiday: tree lightings, Santa, parades, light shows, New Year's Eve, seasonal festivals.
- Comedy: stand-up, comedy shows, magic/comedy shows.
- Stage: theater, ballet, orchestra and symphony, choirs, ticketed concerts that aren't bar gigs.
- Family: kids' events, family movie nights, teas, fishing rodeos for kids, 5Ks.
- Tastings: wine, beer, bourbon, food festivals and tastings. Mark 21+ in `ages`.
- Markets: craft shows, holiday markets, farmers markets with a dated event.

## What to leave out

- Live music bar gigs (they come from `destin.json`).
- Anything past, canceled or postponed. Recheck every event already in the file; remove it if its source
  no longer confirms it.
- Events with no named date (e.g. "Fridays this fall" with no confirmed dates).
- Okaloosa County's text-alert service. Never mention it.

## Recurring events

Use one entry with `start_date`, `end_date` and `repeats`:
- `"daily"` · a day name like `"Sat"` or `"Fri"` · several like `"Sat/Sun"` · a range like `"Thu-Sat"`.
- The page shows the event on every matching day inside the dates. Leave `repeats` empty for one-time
  and multi-day events (it then shows every day from start to end).

## Writing style

Neutral and factual. No hype, no commentary on venues or organizers. American spelling.
Leave anniversary numbers ("40th annual") out of `event`; put them in `notes` if they matter.

## Format

```json
{
  "_readme": "What's Good Local weekly events feed for the Destin area (home page guide + WGL-TV guide). Written by the weekly scheduled task; see guide/CLAUDE.md.",
  "updated": "YYYY-MM-DD",
  "events": [
    {
      "category": "Holiday",
      "event": "Santa's Arrival by Boat",
      "venue": "HarborWalk Village",
      "town": "Destin",
      "address": "102 Harbor Blvd, Destin, FL 32541",
      "start_date": "2026-11-28",
      "end_date": "2026-11-28",
      "repeats": "",
      "time": "2 PM",
      "cost": "Free",
      "ages": "All",
      "featured": true,
      "source": "https://organizer-page.example/event",
      "notes": ""
    }
  ]
}
```

- **Required:** `category`, `event`, `venue`, `town`, `start_date`, `end_date`, `time`, `source`.
  Dates are `YYYY-MM-DD`, Central time. `time` is short text ("7 PM", "6–8 PM", "Doors 6; show 8:15 PM").
  If no time is published, use `"See details"`.
- `address` when the source gives one (used for the Directions button and Google's event listing).
- `featured: true` for the 8–12 biggest, most visual events in the window (parades, Santa, tree lightings,
  big shows). These sort to the top.
- Sort by `start_date`, then `event`. Validate with `python3 -m json.tool guide/events.json`.
