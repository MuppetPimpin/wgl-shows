# wgl-shows: the weekly live music feed for What's Good Local

Six files, one per city. Each city's live music page reads its file and adds those shows to the
hand-picked shows that live on the WGL server. **This repo only adds shows. It never removes or
edits a hand-picked show.**

| File | Page that reads it | Hand-picked list on the server (read it, never write it) |
|---|---|---|
| `destin.json` | https://whatsgoodlocal.com/best-live-music-in-destin-tonight/ | the LOCAL_SHOWS list inside that page |
| `pensacola.json` | https://whatsgoodlocal.com/pensacola/live-music/ | https://whatsgoodlocal.com/pensacola/live-music/shows.json |
| `panamacity.json` | https://whatsgoodlocal.com/panama-city-beach/live-music/ | https://whatsgoodlocal.com/panama-city-beach/live-music/shows.json (and tootsies.php for Tootsie's) |
| `tampa.json` | https://tampa.whatsgoodlocal.com/live-music/ | https://tampa.whatsgoodlocal.com/live-music/shows.json |
| `gulfshores.json` | https://whatsgoodlocal.com/gulf-shores/live-music/ | https://whatsgoodlocal.com/gulf-shores/live-music/shows.json |
| `daytona.json` | https://whatsgoodlocal.com/daytona-beach/live-music/ | https://whatsgoodlocal.com/daytona-beach/live-music/shows.json |

The `football/` folder is a separate feed (the weekly football schedule) with its own rules in
`football/CLAUDE.md`. The live music task never touches it.

The `ufc/` folder is a separate feed (the UFC fight schedule, refreshed Monday and Thursday) with its
own rules in `ufc/CLAUDE.md`. The live music task never touches it.

The `wine/` folder is a separate feed (dated wine events for the wine tasting page, refreshed every
Monday) with its own rules in `wine/CLAUDE.md`. The live music task never touches it.

The `foodtrucks/` folder is a separate feed (the Best Food Trucks pages, updated by hand for now) with its
own rules in `foodtrucks/CLAUDE.md`. The live music task never touches it.

The `boardwalk/` folder is a separate feed (dated Pensacola Beach Boardwalk events, refreshed every
Monday) with its own rules in `boardwalk/CLAUDE.md`. The live music task never touches it.

The `casinos/` folder is a separate feed (dated shows and events at the Biloxi and Atmore casinos, refreshed
every Monday) with its own rules in `casinos/CLAUDE.md`. The live music task never touches it.

The `casino-bus/` folder is a separate feed (daily casino bus trips, built automatically by a GitHub
Action from the Casino Trips sheet) with its own notes in `casino-bus/CLAUDE.md`. No scheduled task
touches it.

## The one rule: no source, no listing

Every show needs a `source`: an https link to a venue calendar, the band's own show page, an event
page, or a ticket page that **states this date** for this act at this venue. If the date can't be
confirmed on that page, leave the show out. A wrong show is worse than a missing one.

## What to include

- Live music in the next 21 days (from the run date), in or near that city:
  - Destin: Destin, Miramar Beach, Sandestin/Baytowne, Fort Walton Beach, Okaloosa Island, Niceville, Santa Rosa Beach/30A
  - Pensacola: Pensacola, Pensacola Beach, Perdido Key, Gulf Breeze, Navarre
  - Panama City: Panama City Beach, Panama City, Rosemary/Alys/Inlet Beach
  - Tampa: Tampa, St. Petersburg, Clearwater, the beaches
  - Gulf Shores: Gulf Shores, Orange Beach (including The Wharf), Fort Morgan, Foley. Flora-Bama is in Perdido
    Key, Florida, so it belongs to pensacola.json, not here. Check the beach bars and venues' own calendars every
    week: The Hangout, LuLu's Gulf Shores, Flora-Bama Yacht Club (Orange Beach), Pink Pony Pub, Pirate's Cove
    (Josephine), Big Beach Brewing, Tacky Jacks, The Gulf, Cobalt, Picklemo's, Live Bait, Sea-N-Suds, and the
    free concert series at The Wharf. Shows at the Orange Beach Amphitheater at The Wharf sold through
    Ticketmaster are left out (the page pulls those automatically). Set `town` to Gulf Shores, Orange Beach,
    Fort Morgan or Foley.
  - Daytona Beach: Daytona Beach, Daytona Beach Shores, Ormond Beach, Ponce Inlet, New Smyrna Beach, Flagler Beach.
    Check the beach bars and venues' own calendars every week: Ocean Deck (bands nightly, beach stage Fri–Sun),
    Mai Tai Bar (Ocean Walk), The Beach Bucket (Ormond), Hard Rock Hotel Daytona Beach, Main Street Station and the
    Main Street bars, Johnny D's (Flagler Beach), and the Flagler Avenue and Canal Street bars in New Smyrna. Free
    Bandshell concerts count when a named act and date are posted. Peabody Auditorium, the Ocean Center and
    Speedway shows sold through Ticketmaster are left out. Set `town` to the venue's town (Daytona Beach, Ormond
    Beach, New Smyrna Beach, Flagler Beach, Ponce Inlet). Bike Week and Biketoberfest band lineups count when the
    venue posts the act and date.
- Bar and restaurant gigs, free concert series, festivals, local bands with dated shows.
- Up to 15 shows per city. Prefer variety (different venues and nights) over many shows at one bar.
- **No more than 4 shows at any one venue** per city file.
- **Pensacola:** the page sorts shows into areas (Pensacola, Pensacola Beach, Gulf Breeze & Navarre, Perdido Key),
  so cover all of them, not just downtown. Every week check the beach and outlying venues' own calendars or
  show pages: Bamboo Willie's, Flounder's Chowder House, Bounce Beach and Whiskey Joe's (Pensacola Beach
  Boardwalk), Casino Beach Bar & Grille, Peg Leg Pete's, Paradise Bar & Grill, Red Fish Blue Fish, Sandshaker
  Lounge, Juana's Pagodas (Navarre Beach) and Flora-Bama (Perdido Key). Set `town` to where the venue is
  (Pensacola Beach, Gulf Breeze, Navarre, Perdido Key), never just "Pensacola", for those. A named act on a
  dated night still needs a source that states the date.

## What to leave out

- Anything already in that city's hand-picked list (same band, same day).
- Shows sold through Ticketmaster: the pages already pull those automatically from the
  Ticketmaster API. This covers the Saenger, Vinyl Music Hall and the Bay Center in Pensacola, the
  big arenas and amphitheaters in Tampa, and similar ticketed venues.
- Karaoke, DJ-only nights, trivia, open mics with no named act.
- Recurring "live music every Friday" listings with no named act for a specific date.
- Anything past, canceled or postponed.

## Writing style for `when`, `tag`, `details`, `blurb`

Neutral and factual. No hype, and no commentary on venues or bands. American spelling. Do not
mention Okaloosa County's text-alert service.

## Format (one file per city)

```json
{
  "_readme": "What's Good Local weekly show feed for <city>. Written by the weekly scheduled task; see CLAUDE.md.",
  "updated": "YYYY-MM-DD",
  "shows": [
    {
      "kind": "free",
      "band": "Band Name",
      "venue": "Venue Name",
      "town": "Destin",
      "when": "Fri Oct 23 · 7 PM",
      "start": "2026-10-23T19:00",
      "end": "2026-10-23T22:00",
      "address": "123 Harbor Blvd, Destin, FL 32541",
      "source": "https://venue.com/calendar",
      "free": true
    }
  ]
}
```

- **Required:** `band`, `venue`, `town`, `when`, `start`, `end`, `source`. The page drops a show
  that's missing any of these.
- `start` and `end` use local time in the format `YYYY-MM-DDTHH:MM`. Central time for Destin,
  Pensacola, Panama City and Gulf Shores; Eastern for Tampa and Daytona Beach. If the source gives no end time, use start + 3 hours.
  If the source gives no start time, leave the show out.
- `kind`: `"concert"` only when the show needs a ticket bought in advance; everything else is `"free"`.
  The page shows a "🎸 Live music" label on these. Add `"free": true` only when the source says there's no cover.
- Optional: `with` (opening acts), `tag` (short line, like "Sunset series"), `details`
  (cover, ages, doors), `address` (for the Directions button), `tickets` (https ticket link),
  `url` (https page for "Full lineup"), `img` (https image URL from the venue or band, only if
  clearly theirs to share), `blurb` (one or two sentences, only shown if the show gets the big card),
  `drive` (short note if the venue is outside the main town).
- Every link must start with `https://`.
- Do not use `nights`, `feature` or `bandUrl`. The page ignores them.
- Sort shows by `start`. Keep the JSON valid (check it with `python3 -m json.tool`).
