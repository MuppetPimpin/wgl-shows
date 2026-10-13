# football/: the weekly football schedule for What's Good Local

One file, `football/schedule.json` in the wgl-shows repo, shared by three "Where to Watch Football" pages. All three cities are on
Central Time, so one schedule serves them all.

| Page that reads it | Where the page lives |
|---|---|
| https://whatsgoodlocal.com/game-day/where-to-watch-football-in-destin/ | WordPress post |
| https://whatsgoodlocal.com/pensacola/where-to-watch-football/ | static page on the server |
| https://www.panamacity.whatsgoodlocal.com/where-to-watch-football/ | static page on the server |

Each page fetches `schedule.json` from this repo and builds its scoreboard, "Watch parties this week",
the streaming-only list and the "Big games ahead" table from it. **This folder only holds the
schedule. Never touch the live music files at the top of this repo. Never edit the pages, the bars or the team tables; they live on the WGL servers.**

## The one rule: verified games only

Every game needs a `source`: an https page or ESPN data feed you actually opened that shows **this
matchup on this date** with this kickoff time and network. If the kickoff time isn't set yet, write
`"TBA"`. If you can't confirm a game, leave it out. A wrong kickoff time is worse than a missing game.

Good sources (ESPN's schedule pages often load empty; the data feed behind them works):
- NFL week: `https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=2026&seasontype=2&week=<N>`
- College week: `https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?dates=2026&seasontype=2&week=<N>&groups=80&limit=300`
- AP rankings: `https://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings`
- Team schedules (for big games): `https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/<id>/schedule?season=2026`
- For `source`, use the matching human page, e.g. `https://www.espn.com/nfl/schedule/_/week/6/year/2026/seasontype/2`.
- Bowl games and the College Football Playoff use `seasontype=3` (postseason); NFL playoffs too.

## The window

From the run date (Monday) through the following Monday: 8 days, so both Monday Night Football games
show. Past games hide themselves on the page, so nothing goes stale during the week.

## Times

`time` is **Central**, 24-hour `"HH:MM"`, or `"TBA"`. ESPN's feed gives UTC: Central is UTC−5 until
Sunday Nov 1, 2026 at 2am, then UTC−6. Convert each game by its own date. Double-check a few against
a page that prints ET (ET minus one hour = CT).

## What to include

- **NFL:** every game in the window, including London/international games (put the stadium in
  `where`). List bye teams in `byes` (full team names).
- **College, weeknights (Tue–Fri):** games on a national channel (ABC, CBS, NBC, FOX, ESPN, ESPN2,
  ESPNU, CBSSN, FS1, SEC Network, ACC Network, Big Ten Network). Skip streaming-only weeknight games
  unless a team in the Saturday list below is playing.
- **College, Saturday:** up to 22 games: every game with an AP Top 25 team, every SEC game, and any
  game involving Florida State, Miami, USF, UCF, FIU, FAU, South Alabama, Troy, Southern Miss,
  Louisiana, or Clemson. Then fill with the best national-TV games.
- **Postseason:** conference championships, every College Football Playoff game, bowl games involving
  the teams above, NFL playoffs and the Super Bowl.
- **Off-season:** when there are no games in the window, write `"games": []`. The page shows "Next
  week's games post Monday".

## Team names (the pages match on these, so keep them exact)

- NFL: full name, e.g. `"New Orleans Saints"`, `"Tampa Bay Buccaneers"`.
- College: the short school name ESPN uses without the mascot: `"Florida"`, `"Florida State"`,
  `"Alabama"`, `"Auburn"`, `"LSU"`, `"Ole Miss"`, `"Mississippi State"`, `"Georgia"`, `"Tennessee"`,
  `"Miami"`, `"USF"`, `"UCF"`, `"South Alabama"`, `"Texas A&M"`, `"Oklahoma"`, `"Clemson"`.
- Ranks go in `away_rank` / `home_rank` (AP poll), not in the name.

## `big` (gold on the scoreboard)

`true` for: Thursday, Sunday and Monday night NFL games; any NFL game with the Saints; any college
game between two ranked teams; any game involving Alabama, Auburn, Florida, Florida State, LSU,
Ole Miss or Georgia; rivalry games (Iron Bowl, Egg Bowl, Florida–Georgia, Florida–FSU, FSU–Miami);
championship and playoff games. Everything else `false`. Aim for 8–14 big games in a normal week.

## `streaming`

`true` only when the game is on no TV channel at all: Prime Video, Netflix, Peacock, ESPN+, YouTube,
Apple TV and similar. A game on ESPN that also streams on ESPN+ is `false`.

## `big_games` (the "Big games ahead" table)

The marquee games still to come this season, after the window: Florida–Georgia, Alabama–LSU, the
Iron Bowl, the Egg Bowl, Florida–FSU, Thanksgiving NFL, the SEC Championship, the College Football
Playoff, the Super Bowl. Each week: drop games that have been played, fill in `time` and `tv` once
they're announced (they're usually set 6 to 12 days ahead), and add postseason games once dates and
matchups are set. Keep it to about 20, sorted by date. Same `source` rule.

## Format

```json
{
  "_readme": "What's Good Local weekly football schedule, shared by the Destin, Pensacola and Panama City Beach pages. All times Central. Written by the Monday scheduled task; see CLAUDE.md.",
  "updated": "YYYY-MM-DD",
  "week_start": "YYYY-MM-DD",
  "week_end": "YYYY-MM-DD",
  "nfl_week": 7,
  "cfb_week": 8,
  "byes": ["Cincinnati Bengals"],
  "games": [
    {
      "league": "NFL",
      "date": "2026-10-18",
      "time": "12:00",
      "away": "Chicago Bears",
      "home": "Atlanta Falcons",
      "away_rank": null,
      "home_rank": null,
      "where": null,
      "tv": "FOX",
      "streaming": false,
      "big": false,
      "source": "https://www.espn.com/nfl/schedule/_/week/6/year/2026/seasontype/2"
    }
  ],
  "big_games": [
    {
      "date": "2026-10-31",
      "time": "14:30",
      "game": "Florida vs. Georgia",
      "where": "Atlanta (Mercedes-Benz Stadium)",
      "tv": "ABC",
      "source": "https://..."
    }
  ]
}
```

- `league` is `"NFL"` or `"CFB"`. `where` is `null` unless it's a neutral site (then the page writes
  "vs." instead of "at" and shows the place).
- `tv`: the network as fans say it: `"ESPN"`, `"ABC"`, `"SEC Network"`, `"Prime Video"`,
  `"ESPN / ABC"` for a simulcast.
- Sort `games` by `date`, then `time` (`"TBA"` last in its day). Sort `big_games` by date.
- Every link starts with `https://`. Keep the JSON valid: `python3 -m json.tool schedule.json`.
- Writing is neutral and factual. American spelling.
