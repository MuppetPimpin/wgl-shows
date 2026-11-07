# wine/: the wine events feed for What's Good Local

One file, `wine/events.json`. It feeds:

| Page that reads it | What it shows |
|---|---|
| https://whatsgoodlocal.com/wine-tasting/ | The "Upcoming wine events" cards, the next-event line, and the Event schema Google reads |

The page loads it from
`https://cdn.jsdelivr.net/gh/MuppetPimpin/wgl-shows@main/wine/events.json`.
The tasting rooms, festival cards and FAQ on that page live on the WGL server, not here.
**This folder only holds dated wine events. Never touch the live music files, `football/`, `guide/`,
`ufc/`, `deals/` or `casino-bus/`, and never edit any page on the WGL servers.**

A scheduled task refreshes this file every Monday.

## The one rule: no source, no listing

Every event needs a `source`: an https link to the organizer's, venue's or official ticket page
(Big Tickets, Eventbrite, the venue's own calendar, a chamber listing posted by the business) that
**states this date** for this event. Aggregators and rental-company "events" pages (destinmiramar.com,
destinvacation.com, beachguide.com, rental blogs) are leads only. They have printed wrong dates
before (Nov 6, 2026: one listed Seeing Red as Nov 5–15 when the festival page says Nov 5–8, and the
Pensacola Beach Art & Wine Festival in November when it's held in May). Open the organizer's page and
confirm. A venue's or organizer's own Instagram post that states the date counts as a source (cloud runs can't
open Instagram, so keep any Instagram-sourced entry until its date passes unless another source cancels it).
SoWal.com event pages count as a source only when they're the dated listing for that exact
date. If the date can't be confirmed, leave the event out. A wrong date is worse than a missing event.

## Window and area

- Run date through **180 days out** (wine festivals sell tickets months ahead). Drop anything whose
  `end_date` is before the run date.
- Area: Destin, Miramar Beach, Sandestin / Village of Baytowne Wharf / Grand Boulevard, Fort Walton
  Beach, Okaloosa Island, Niceville, Santa Rosa Beach / 30A (Grayton, Seaside, WaterColor, Gulf Place,
  Alys Beach, Rosemary Beach), Navarre. Pensacola Beach and Panama City Beach only for big festivals,
  with a `drive` note.
- Up to 25 events. Every big festival in the window goes in; fill the rest with walks, dinners and tastings.

## What counts

`kind` is exactly one of:

- `Festival`: multi-event wine festivals (Seeing Red, 30A Wine Festival, Sandestin Wine Festival,
  South Walton Beaches Wine & Food Festival, Harvest Wine & Food Festival, Pensacola Beach Art & Wine).
- `Wine walk`: strolls with pours at several stops (Grayton Beach Wine Walk, Gulf Place Wine Walk,
  Rosemary Beach Uncorked, Sparkling Wine & Holiday Lights).
- `Wine dinner`: paired winemaker or vintner dinners at a restaurant or resort.
- `Tasting`: ticketed or free in-store tastings at a named shop, winery or bar.
- `Charity`: auctions and galas built around wine (Destin Charity Wine Auction).

Leave out: beer/bourbon-only events, "wine specials" and happy hours with no event, and anything past,
canceled or postponed. Recheck every event already in the file; remove it if its source no longer
confirms it.

## Recurring events

Wine walks repeat (Grayton: third Thursday, $25, Shacks Art. Gulf Place: fourth Thursday, free,
Spires Lane, per @gulfplace on Instagram, June 22, 2026; check gulfplaceon30a.com for a dated post). Add **one entry per confirmed date** and only for
dates a source actually lists. Don't project a pattern forward.

## Writing style

Neutral and factual. No hype, no commentary on venues, organizers or other sites. American spelling.
Never mention Okaloosa County's text-alert service. Leave anniversary numbers ("34th annual") out of
`event`; put them in `notes` if they matter.

## Format

```json
{
  "_readme": "What's Good Local wine events feed (whatsgoodlocal.com/wine-tasting/). Written by the weekly scheduled task; see wine/CLAUDE.md in github.com/MuppetPimpin/wgl-shows.",
  "updated": "YYYY-MM-DD",
  "events": [
    {
      "kind": "Wine walk",
      "event": "Grayton Beach Wine Walk",
      "venue": "Shacks Art",
      "town": "Grayton Beach",
      "address": "14 Clayton Ln, Grayton Beach, FL 32459",
      "start_date": "2026-12-17",
      "end_date": "2026-12-17",
      "time": "5–7 PM",
      "start": "2026-12-17T17:00",
      "cost": "$25",
      "ages": "21+",
      "featured": false,
      "blurb": "Wine and bites at six Grayton merchants, then dessert, live music and a raffle on the Shacks deck.",
      "tickets": "",
      "source": "https://sowal.com/node/156254",
      "drive": "",
      "notes": ""
    }
  ]
}
```

- **Required:** `kind`, `event`, `venue`, `town`, `start_date`, `end_date`, `time`, `source`.
  The page drops an event missing any of these.
- Dates are `YYYY-MM-DD`. `start` is optional local Central time `YYYY-MM-DDTHH:MM` (used for Google's
  event listing); leave it `""` if the source gives no start time.
- `time`: short and readable ("5–7 PM", "1–4 PM", "Times vary by event").
- `cost`: as the source prints it ("$25", "$225 GA · $350 VIP"); `"See tickets"` if not printed.
- `featured: true` for the big festivals and Rosemary Beach Uncorked–size events (max 4).
- `blurb`: one sentence, only facts from the source. `tickets`: https ticket link if different from
  `source`. `drive`: e.g. "About 1 hr 15 min west of Destin" for Pensacola Beach.
- Sort by `start_date`. Every link starts with `https://`.
  Validate: `python3 -m json.tool wine/events.json`.
