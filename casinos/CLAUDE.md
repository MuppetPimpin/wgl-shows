# casinos/: upcoming shows and events at the casinos WGL covers

One file, `casinos/events.json`. Each WGL casino page shows the next events for its own casino(s)
from it, through the casino events widget, and adds them to Google's event listings. The pages load it from
`https://cdn.jsdelivr.net/gh/MuppetPimpin/wgl-shows@main/casinos/events.json`.

| `casino` slug | Casino | Page(s) that show it |
|---|---|---|
| `hard-rock` | Hard Rock Hotel & Casino Biloxi (Hard Rock Live) | /casinos/ Hard Rock Biloxi page, nearest-casino post |
| `beau-rivage` | Beau Rivage Resort & Casino, Biloxi (Beau Rivage Theatre) | /casinos/beau-rivage-from-florida/, nearest-casino post |
| `ip` | IP Casino Resort Spa, Biloxi | /casinos/ip-casino-biloxi/, nearest-casino post |
| `boomtown` | Boomtown Casino Biloxi | /casinos/boomtown-casino-biloxi/, nearest-casino post |
| `golden-nugget` | Golden Nugget Biloxi | nearest-casino post |
| `wind-creek-atmore` | Wind Creek Casino & Hotel, Atmore, AL | /casinos/wind-creek-atmore-from-pensacola/, closest-casino-to-Pensacola, nearest-casino post |

**This folder only holds dated casino events. Never touch the live music files, `football/`, `guide/`, `ufc/`,
`wine/`, `deals/`, `foodtrucks/`, `boardwalk/` or `casino-bus/`, and never edit any page on the WGL servers.**
A scheduled task refreshes this file every Monday.

## The one rule: no source, no listing

Every event needs a `source`: an https link to the casino's own entertainment/events/promotions page (or the
official ticket page it links to) that **states this date**. Aggregators (Songkick, Bandsintown, ticket resale
sites, concert listing blogs) are leads only. A wrong date is worse than a missing event.

## What to include

- Run date through **90 days out**. Drop anything whose `end_date` has passed, and anything canceled or postponed.
- `kind` is exactly one of: `Concert`, `Comedy`, `Show` (tribute acts, theater, magic), `Fight` (boxing, MMA),
  `Holiday` (New Year's Eve, fireworks, holiday events), `Promotion` (a dated giveaway, drawing, free-play or
  buffet special with a stated date, open to the public).
- Up to 8 events per casino, 40 total. Prefer headliners and dated promotions over weekly lounge bands.
- Leave out: weekly lounge/bar bands with no named act, bingo, tournaments for members only, anything that
  needs a players-club tier to qualify, and anything with no stated date.
- Recurring promotions: one entry per stated date, never project a pattern.

## Writing style

Neutral and factual. No hype, no commentary on the casinos or acts. American spelling. Leave ticket prices out
unless the casino's page prints them. Never mention Okaloosa County's text-alert service.

## Format

```json
{
  "_readme": "What's Good Local casino events feed. Written by the weekly scheduled task; see casinos/CLAUDE.md in github.com/MuppetPimpin/wgl-shows.",
  "updated": "YYYY-MM-DD",
  "events": [
    {
      "casino": "hard-rock",
      "kind": "Concert",
      "event": "Act Name",
      "venue": "Hard Rock Live",
      "start_date": "2026-12-05",
      "end_date": "2026-12-05",
      "time": "8 PM",
      "start": "2026-12-05T20:00",
      "cost": "",
      "featured": false,
      "blurb": "",
      "tickets": "https://...",
      "source": "https://..."
    }
  ]
}
```

- **Required:** `casino`, `kind`, `event`, `venue`, `start_date`, `end_date`, `time`, `source`. The widget drops an
  event missing any of these.
- `casino` must be one of the slugs in the table above.
- Times are local: Central for Biloxi and Atmore. `start` is `YYYY-MM-DDTHH:MM`, or `""` if no time is printed.
- `featured: true` for big headliners and New Year's Eve, max 6.
- `blurb`: one sentence of facts from the source, or `""`.
- Sort by `start_date`. Every link starts with `https://`. Validate: `python3 -m json.tool casinos/events.json`.
