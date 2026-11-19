# boardwalk/: the Pensacola Beach Boardwalk events feed for What's Good Local

One file, `boardwalk/events.json`. It feeds:

| Page that reads it | What it shows |
|---|---|
| https://whatsgoodlocal.com/pensacola-beach-boardwalk/ | "Tonight at the Boardwalk", the 14-day calendar, the "Coming up" list, and the Event schema Google reads |

The page loads it from
`https://cdn.jsdelivr.net/gh/MuppetPimpin/wgl-shows@main/boardwalk/events.json`.
The page also pulls Boardwalk shows out of `pensacola.json` (the live music feed) on its own, so a show
that's already in `pensacola.json` does not need to be repeated here. The business listings, yearly event
cards and FAQ on that page live on the WGL server, not here.
**This folder only holds dated Boardwalk events. Never touch the live music files, `football/`, `guide/`,
`ufc/`, `wine/`, `deals/`, `foodtrucks/` or `casino-bus/`, and never edit any page on the WGL servers.**

A scheduled task refreshes this file every Monday.

## The one rule: no source, no listing

Every event needs a `source`: an https link to the organizer's or venue's own page that **states this date**
for this event. Good sources: pensacolabeachboardwalk.com (Happenings, Dining, Shopping pages), the
Pensacola Beach Chamber of Commerce (visitpensacolabeach.com) and its press releases, visitpensacola.com event
pages posted by the organizer, the venue's own site or calendar, the band's own show page, and ticket pages.
Aggregators and rental-company or listicle pages (pensacolabeach.com month roundups, beachguide.com,
tripshock.com) are leads only: they have carried last year's dates. Open the organizer's page and confirm.
If the date can't be confirmed, leave the event out. A wrong date is worse than a missing event.

The Boardwalk's own Happenings page is https://www.pensacolabeachboardwalk.com/happenings/index.html.
Check it first every run, and check the year on every date. WebFetch has returned an old cached copy of
this page (the 2025 schedule) while the live page showed 2026; if the copy you get shows last year's
dates, refetch it with a cache-busting query (…/happenings/index.html?v=YYYYMMDD) and try
https://pensacolabeachboardwalk.com/happenings before concluding nothing is posted. Never copy a date
from it unless the year printed is the current one. Its usual
December lineup (watch for the new-year versions): Photos with Santa (Saturdays and Sundays), Jacoby's
Sounds of the Season (Saturdays), Sip and Shop at Envie Boutique and at Ardor Boutique, Holiday Specials at
Ardor Boutique, the Lighted Boat Parade (with a kids' pre-parade party, Santa at the Quietwater shell and
fireworks over the Sound), and New Year's Eve fireworks at midnight.

Holiday events are announced late. The Lighted Boat Parade, Surfin' Santa Parade, Photos with Santa and
New Year's Eve fireworks only go in once a source states the current year's date. They also get rescheduled
for weather (the 2025 boat parade moved from Dec 5 to Dec 12), so recheck them every run.

## Window and area

- Run date through **60 days out**. Drop anything whose `end_date` is before the run date.
- Area: the Pensacola Beach Boardwalk and Quietwater Beach (400 and 800 Quietwater Beach Road), plus events
  that start, end or are watched from the Boardwalk (the Lighted Boat Parade, Surfin' Santa Parade, New
  Year's Eve fireworks over the Santa Rosa Sound).
- Venues on the Boardwalk: Bamboo Willie's, Bounce Beach Pensacola, Flounder's Chowder House (next door at
  800 Quietwater), Whiskey Joe's, Cafe Nola, Señor Frog's, Papa's Pizza, Hooters, Kilwins, Ron Jon Surf Shop,
  Intracoastal Outfitters, Envie Boutique, Ardor Boutique, Premier Dolphin Cruise, Pensacola Bay City Ferry,
  the Quietwater Beach shell stage.
- Up to 30 events.

## What counts

`kind` is exactly one of:

- `Holiday`: boat parade, Santa, parades, fireworks, New Year's Eve, Halloween (Beach-O-Ween).
- `Festival`: Crawfish Festival, Songwriters Festival nights at Boardwalk venues, Art & Wine Festival, Taste of the Beach events held on the Boardwalk.
- `Live music`: a named act on a stated date at a Boardwalk venue. Recurring "live music nightly" with no named act does not count (the page already shows that).
- `Family`: kids' events, Snowbird Beach Bash, free community events on the Boardwalk.
- `Shopping`: dated store events (sip and shops, holiday sales with stated dates).

Leave out: karaoke, trivia, DJ-only nights, happy hours with no event, anything past, canceled or postponed.
Recheck every event already in the file; remove it if its source no longer confirms it.

## Recurring events

Add **one entry per confirmed date**, only for dates a source actually lists (Photos with Santa on
Dec 5, 12 and 19 = three entries). Don't project a pattern forward.

## Writing style

Neutral and factual. No hype, no commentary on venues, organizers or other sites. American spelling.
Never mention Okaloosa County's text-alert service. Leave anniversary numbers ("27th annual") out of `event`.

## Format

```json
{
  "_readme": "What's Good Local Pensacola Beach Boardwalk events feed (whatsgoodlocal.com/pensacola-beach-boardwalk/). Written by the weekly scheduled task; see boardwalk/CLAUDE.md in github.com/MuppetPimpin/wgl-shows.",
  "updated": "YYYY-MM-DD",
  "events": [
    {
      "kind": "Holiday",
      "emoji": "🛥️",
      "event": "Lighted Boat Parade",
      "venue": "Santa Rosa Sound by the Boardwalk",
      "start_date": "2026-12-11",
      "end_date": "2026-12-11",
      "time": "6:30 PM",
      "start": "2026-12-11T18:30",
      "cost": "Free",
      "featured": true,
      "blurb": "Decorated boats leave Sabine Marina and loop the Santa Rosa Sound by the Boardwalk, then Santa greets kids at the Quietwater Beach shell.",
      "source": "https://www.visitpensacola.com/events/..."
    }
  ]
}
```

- **Required:** `kind`, `event`, `venue`, `start_date`, `end_date`, `time`, `source`. The page drops an
  event missing any of these.
- Dates are `YYYY-MM-DD`. `start` is optional local Central time `YYYY-MM-DDTHH:MM`; leave it `""` if the
  source gives no start time.
- `emoji`: one emoji for the calendar (🎸 live music, 🛥️ boat parade, 🎅 Santa, 🎆 fireworks, 🦞 crawfish,
  🛍️ shopping, 🎉 everything else).
- `time`: short and readable ("6:30 PM", "10:30 AM–3:30 PM", "Midnight").
- `cost`: as the source prints it ("Free", "$20"); `""` if not printed. Write exactly "Free" when the source says free or no cover.
- `performer`: the named band or artist, only when the source names one (for Google's event listing).
- `featured: true` for the big ones (boat parade, Surfin' Santa, New Year's Eve fireworks, Crawfish
  Festival). Max 5. Featured events also show in the page's "Coming up" list beyond the 14-day calendar.
- `blurb`: one sentence, only facts from the source.
- Sort by `start_date`. Every link starts with `https://`.
  Validate: `python3 -m json.tool boardwalk/events.json`.
