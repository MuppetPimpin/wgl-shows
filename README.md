# wgl-shows

Weekly live music feed for What's Good Local. One JSON file per city (`destin.json`, `pensacola.json`, `panamacity.json`, `tampa.json`), refreshed every week by a scheduled task. Each city's live music page reads its file and adds these shows to its hand-picked list. Rules and format are in `CLAUDE.md`.

`casino-bus/trips.json` is a separate daily feed of Good Time Tours casino bus trips, built by a GitHub Action (see `casino-bus/CLAUDE.md`).

`ufc/schedule.json` is the UFC fight schedule for the Where to Watch UFC page, refreshed Monday and Thursday by a scheduled task (see `ufc/CLAUDE.md`).

`wine/events.json` is the wine events feed for whatsgoodlocal.com/wine-tasting/ (wine walks, festivals, wine dinners and tastings), refreshed every Monday by a scheduled task (see `wine/CLAUDE.md`).
