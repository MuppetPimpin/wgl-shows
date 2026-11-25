Weekly live music feed update for What's Good Local's Gulf & Texas towns.

1. Clone or pull github.com/MuppetPimpin/wgl-shows and read CLAUDE.md in full. It is the rulebook: follow it exactly (no source, no listing; next 21 days from today; up to 15 shows per city; no more than 4 per venue; leave out Ticketmaster, karaoke, DJ-only, trivia, open mics and anything already in the city's hand-picked list; format, time zone and writing-style rules).

2. This task covers ONLY these city files (other regions have their own tasks running at the same time, so never touch any other file or folder):
   - galveston.json  (Galveston Island: Central time)
   - mscoast.json  (the Mississippi Gulf Coast: Central time)
   - portaransas.json  (Port Aransas: Central time)
   - southpadre.json  (South Padre Island: Central time)
   More Gulf & Texas towns will be added to this list as their pages go live; each has its own row in the CLAUDE.md table and its own venue list under "What to include".

3. For each file: read the hand-picked list named in the CLAUDE.md table (shows.json on whatsgoodlocal.com; it may not exist yet, which is fine) so you skip duplicates. Check every venue or calendar named for that town under "What to include" first, then search for more dated shows (venue calendars, band show pages, event pages, ticket pages that are not Ticketmaster). Every show needs an https `source` page that states that act, that venue and that date. Spread your time evenly across the towns.

4. Write each file with "updated" set to today's date (YYYY-MM-DD) and shows sorted by start. Validate each file with python3 -m json.tool. If you could not confirm any shows for a town, write an empty "shows" list rather than guessing.

5. Commit only the files listed above with a message like "Weekly live music (Gulf & Texas): galveston (N), mscoast (N), portaransas (N), southpadre (N)" and push to main. If the push is rejected because another region's task pushed first, run git pull --rebase and push again. Then run git fetch origin main and confirm origin/main has your commit; if it still fails, say so at the top of your summary with the exact git error.

6. Finish with a short summary: shows per town, venues checked, and any venue whose calendar could not be read. Keep wording neutral and never mention Okaloosa County's text-alert service.
