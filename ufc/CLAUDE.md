# ufc/: the UFC fight schedule for What's Good Local

One file, `ufc/schedule.json` in the wgl-shows repo. It feeds:

| Page that reads it | Where the page lives |
|---|---|
| https://whatsgoodlocal.com/game-day/where-to-watch-ufc-in-destin/ | WordPress page (one Elementor HTML block) |

The page fetches `schedule.json` from this repo and builds its fight cards, the "Next fight" line in
the hero and the Google event listings from it. **This folder only holds the schedule. The bars on
the page live on the WGL server. Never touch the live music files, `football/`, `guide/`, `deals/`
or `casino-bus/`, and never edit any page on the WGL servers.**

A scheduled task refreshes this file every Monday and Thursday (Thursday catches fight-week changes
before Saturday cards).

## The one rule: no source, no listing

Every event needs a `source`: the event's own page on ufc.com (`https://www.ufc.com/event/...`).
It must show **this event on this date**. Use ufc.com/events to find the list, then open each event
page for the card and the times. Wikipedia, schedule sites and news articles are leads only — when
they disagree with ufc.com, ufc.com wins. If an event can't be confirmed on ufc.com, leave it out.
A wrong fight is worse than a missing one.

## What to include

- Every UFC event (numbered events and Fight Nights) from the run date through the next **120 days**,
  up to 12 events, sorted by date.
- Drop events that are over, canceled or no longer on ufc.com.
- When a bout falls off a card, update `main` / `co_main` to match ufc.com. If ufc.com shows
  "TBD vs TBD", set `main` to `""` (the page shows "Main event to be announced").

## Times

All times are **Central**, 24-hour `"HH:MM"`. ufc.com prints Eastern (ET minus one hour = CT).
`date` is the U.S. date of the card (for Australia/Asia cards, the U.S. date, not the local date).
If ufc.com shows no time for a segment, use `null`. If it shows no main card time at all, set
`main_card` to `"TBA"`. ufc.com's events list sometimes shows times that conflict with the event
page — **always use the event page**.

## Format

```json
{
  "_readme": "What's Good Local UFC schedule. All times Central. Written by the Monday/Thursday scheduled task; see ufc/CLAUDE.md in github.com/MuppetPimpin/wgl-shows.",
  "updated": "YYYY-MM-DD",
  "events": [
    {
      "date": "2026-11-14",
      "event": "UFC 334",
      "kind": "numbered",
      "main": "Ciryl Gane vs. Josh Hokit",
      "main_short": "Gane vs. Hokit",
      "title_fight": "Heavyweight title",
      "co_main": "Kayla Harrison vs. Amanda Nunes",
      "venue": "Madison Square Garden",
      "city": "New York, NY",
      "early_prelims": "16:00",
      "prelims": "18:00",
      "main_card": "20:00",
      "tv": "Paramount+",
      "source": "https://www.ufc.com/event/ufc-334"
    }
  ]
}
```

- `kind`: `"numbered"` (UFC 334, UFC 335…) or `"fight_night"`.
- `main`: full names as ufc.com prints them, joined with " vs. ". `main_short`: last names only.
- `title_fight`: e.g. `"Heavyweight title"`, `"Women's bantamweight title"`, or `null`.
- `co_main`: full names, or `null` if ufc.com doesn't show a clear second bout.
- `city`: "City, ST" in the U.S.; "City, Country" abroad.
- `tv`: `"Paramount+"`, or `"Paramount+ / CBS"` when ufc.com lists CBS for that card.
- Every link starts with `https://`. Keep the JSON valid: `python3 -m json.tool ufc/schedule.json`.
- Writing is neutral and factual. American spelling.
