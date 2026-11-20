# wgl-shows

Weekly live music feed for What's Good Local. One JSON file per city (`destin.json`, `pensacola.json`, `panamacity.json`, `tampa.json`), refreshed every week by a scheduled task. Each city's live music page reads its file and adds these shows to its hand-picked list. Rules and format are in `CLAUDE.md`.

`casino-bus/trips.json` is a separate daily feed of Good Time Tours casino bus trips, built by a GitHub Action (see `casino-bus/CLAUDE.md`).

`ufc/schedule.json` is the UFC fight schedule for the Where to Watch UFC page, refreshed Monday and Thursday by a scheduled task (see `ufc/CLAUDE.md`).

`wine/events.json` is the wine events feed for whatsgoodlocal.com/wine-tasting/ (wine walks, festivals, wine dinners and tastings), refreshed every Monday by a scheduled task (see `wine/CLAUDE.md`).

`boardwalk/events.json` is the Pensacola Beach Boardwalk events feed for whatsgoodlocal.com/pensacola-beach-boardwalk/ (holiday events, festivals and named live music on the Boardwalk), refreshed every Monday by a scheduled task (see `boardwalk/CLAUDE.md`).

`casinos/events.json` is the casino events feed (shows, concerts and dated promotions at the Biloxi and Atmore casinos) for the WGL casino pages, refreshed every Monday by a scheduled task (see `casinos/CLAUDE.md`).
