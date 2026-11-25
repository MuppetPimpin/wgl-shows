# wgl-shows: the weekly live music feed for What's Good Local

Ten files, one per city. Each city's live music page reads its file and adds those shows to the
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
| `galveston.json` | https://whatsgoodlocal.com/galveston/live-music/ | https://whatsgoodlocal.com/galveston/live-music/shows.json |
| `staugustine.json` | https://whatsgoodlocal.com/st-augustine/live-music/ | https://whatsgoodlocal.com/st-augustine/live-music/shows.json |
| `fortmyers.json` | https://whatsgoodlocal.com/fort-myers/live-music/ | https://whatsgoodlocal.com/fort-myers/live-music/shows.json |
| `spacecoast.json` | https://whatsgoodlocal.com/space-coast/live-music/ | https://whatsgoodlocal.com/space-coast/live-music/shows.json |
| `myrtlebeach.json` | https://whatsgoodlocal.com/myrtle-beach/live-music/ | https://whatsgoodlocal.com/myrtle-beach/live-music/shows.json |
| `outerbanks.json` | https://whatsgoodlocal.com/outer-banks/live-music/ | https://whatsgoodlocal.com/outer-banks/live-music/shows.json |
| `virginiabeach.json` | https://whatsgoodlocal.com/virginia-beach/live-music/ | https://whatsgoodlocal.com/virginia-beach/live-music/shows.json |
| `oceancitymd.json` | https://whatsgoodlocal.com/ocean-city-md/live-music/ | https://whatsgoodlocal.com/ocean-city-md/live-music/shows.json |
| `jacksonville.json` | https://whatsgoodlocal.com/jacksonville/live-music/ | https://whatsgoodlocal.com/jacksonville/live-music/shows.json |
| `palmbeach.json` | https://whatsgoodlocal.com/palm-beach/live-music/ | https://whatsgoodlocal.com/palm-beach/live-music/shows.json |

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
  - Galveston: Galveston Island (the Strand, downtown, the Seawall, Pier 21, the West End). Check the venues' own
    calendars every week: Old Quarter Acoustic Cafe (413 20th St), Yaga's Cafe (the Strand), Jigger's Lounge
    (Seawall Blvd), Galveston Island Brewing, The Tremont House lobby bar, Hotel Lucine, Saengerfest Park, and
    The Grand 1894 Opera House (only shows it sells itself, not through Ticketmaster). Mardi Gras Galveston and
    other festival stages count when a named act and date are posted. Set `town` to Galveston.
  - St. Augustine: downtown St. Augustine, Anastasia Island, St. Augustine Beach, Vilano Beach, Ponte Vedra Beach.
    Start with the city's live music calendar (https://visitstaugustine.com/music/all), which lists shows by venue,
    then check the venues' own calendars: Tradewinds Lounge (bands nightly), The Original Café Eleven, Colonial Oak
    Music Park, Prohibition Kitchen, O.C. White's, Harry's Seafood Bar & Grille, Milltop Tavern, La Cocina at the
    Cellar Upstairs, Pierre's Pub, Meehan's and the Conch House. Shows at the St. Augustine Amphitheatre and Ponte
    Vedra Concert Hall sold through Ticketmaster are left out. Set `town` to St. Augustine, St. Augustine Beach,
    Vilano Beach or Ponte Vedra Beach.
  - Fort Myers: Fort Myers Beach, Sanibel, Captiva, Bonita Beach, and downtown Fort Myers. Start with the Fort
    Myers Beach Chamber's "Who's playing where" page (https://www.fortmyersbeach.org/hos-playing-where-on-fort-myers-beach),
    which links the venues' own calendars: Doc Ford's, Nervous Nellie's, Margaritaville Beach Resort (free
    concerts), The Whale, Dixie Fish Co., Yucatan Beach Stand, La Ola, Lighthouse Tiki Bar, Parrot Key, Wahoo
    Willie's and the Bayside Park concert series. Set `town` to Fort Myers Beach, Sanibel, Captiva, Bonita Beach or
    Fort Myers.
  - Space Coast: Cocoa Beach, Cape Canaveral and Port Canaveral (The Cove), Cocoa Village, Satellite Beach,
    Indialantic, Melbourne. Check the venues' own calendars every week: Coconuts on the Beach, Sandbar Sports Grill,
    Heidi's Jazz Club, the Westgate Cocoa Beach Pier bars, Grills Seafood Deck & Tiki Bar and the other bars at The
    Cove, Lou's Blues (Indialantic), and Cocoa Village and Cocoa Riverfront Park events. Set `town` to the venue's
    town.
  - Myrtle Beach: the Grand Strand, from Little River and North Myrtle Beach through Myrtle Beach, Surfside Beach and
    Garden City to Murrells Inlet and Pawleys Island. Check the venues' own calendars every week: the Murrells Inlet
    MarshWalk bars (Drunken Jack's, Dead Dog Saloon, Wicked Tuna, Creek Ratz), The Bowery and the Myrtle Beach
    Boardwalk bars, Broadway at the Beach, The Market Common, Barefoot Landing (free shows at House of Blues' Sugar
    Shack deck count; ticketed House of Blues and other Ticketmaster shows are left out), and the Ocean Drive shag
    clubs in North Myrtle Beach (Fat Harold's, Duck's, OD Arcade & Lounge). Resident theater productions (Carolina
    Opry, Alabama Theatre, Medieval Times) are left out. Set `town` to the venue's town.
  - Outer Banks: Corolla, Duck, Southern Shores, Kitty Hawk, Kill Devil Hills, Nags Head, Manteo, Hatteras Island and
    Ocracoke. Check the venues' own calendars every week: Outer Banks Brewing Station, Kelly's Restaurant & Tavern,
    Mulligan's, Lucky 12 Tavern, Sandbar & Grille, Jennette's Pier events, the Duck summer concert series at Duck Town
    Park, and Manteo's waterfront concerts. Many places close or cut back in winter, so an empty week is normal off
    season. Set `town` to the venue's town.
  - Virginia Beach: the Oceanfront, the North End, Sandbridge and Chicks Beach. Check the venues' own calendars every
    week: the free Beach Street USA and Oceanfront park stages (24th Street Park, 31st Street Park, 17th Street), the
    Oceanfront hotel and boardwalk bars, Shaka's, Chix on the Beach, Waterman's Surfside Grille and Abbey Road Pub.
    Shows at the amphitheater and Sandler Center sold through Ticketmaster are left out. Set `town` to Virginia Beach.
  - Ocean City, MD: Ocean City, Fenwick Island, West Ocean City and Berlin. Check the venues' own calendars every week:
    Seacrets (bands nightly in season), Fager's Island, Coconuts Beach Bar, BJ's on the Water, Purple Moose Saloon,
    Bourbon Street on the Beach, and the town's free concerts at Sunset Park and Northside Park. Set `town` to the
    venue's town.
  - Jacksonville Beach & Amelia Island: Jacksonville Beach, Neptune Beach, Atlantic Beach, Mayport and Fernandina Beach
    on Amelia Island. Check the venues' own calendars every week: the Beaches Town Center bars (Atlantic Beach and
    Neptune Beach), Lynch's Irish Pub, Ink Factory Brewing, the Jacksonville Beach oceanfront bars, and Fernandina's
    Centre Street bars. Shows at the Jacksonville amphitheaters and arenas sold through Ticketmaster are left out.
    Set `town` to the venue's town.
  - The Palm Beaches: Jupiter, Juno Beach, Palm Beach, West Palm Beach, Lake Worth Beach, Boynton Beach and Delray Beach.
    Check the venues' own calendars every week: Guanabanas and Square Grouper (Jupiter), the Clematis Street bars in
    West Palm Beach (Roxy's Pub, West Palm Beach Cowboy Club), Two George's Waterfront Grille, Boston's on the Beach and
    the Atlantic Avenue bars in Delray Beach, plus free waterfront concerts in West Palm Beach. Shows at the big
    amphitheater and Kravis Center sold through Ticketmaster are left out. Set `town` to the venue's town.
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
  Pensacola, Panama City, Gulf Shores and Galveston; Eastern for Tampa, Daytona Beach, St. Augustine, Fort Myers, the Space Coast, Myrtle Beach, the Outer Banks, Virginia Beach, Ocean City, MD, Jacksonville and the Palm Beaches. If the source gives no end time, use start + 3 hours.
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
