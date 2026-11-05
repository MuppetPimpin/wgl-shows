# wgl-shows

Weekly live music feed for What's Good Local. One JSON file per city (`destin.json`, `pensacola.json`, `panamacity.json`, `tampa.json`), refreshed every week by a scheduled task. Each city's live music page reads its file and adds these shows to its hand-picked list. Rules and format are in `CLAUDE.md`.

`casino-bus/trips.json` is a separate daily feed of Good Time Tours casino bus trips, built by a GitHub Action (see `casino-bus/CLAUDE.md`).
