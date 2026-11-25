Weekly Crazy Good Deals feed update for What's Good Local's California towns.

1. Clone or pull github.com/MuppetPimpin/wgl-shows and read deals/CLAUDE.md in full. It is the rulebook: follow it exactly (no source, no listing; aggregators like Groupon, SweetDeals, SpotDeals, Valpak, Restaurant.com and Viator are hunting grounds only, and every deal must be confirmed on the business's own page, which is the `source`; categories Food, Drinks, Adventures only; never invent a deal, price, day or hour; neutral, factual wording; American spelling; no claims about paid versus unpaid placement).

2. This task covers ONLY these files (other regions have their own tasks running at the same time, so never touch any other file; destin-deals.json has its own task):
   - deals/sandiego-deals.json  (San Diego)
   - deals/orangecounty-deals.json  (Orange County)
   - deals/losangeles-deals.json  (Los Angeles beaches)
   - deals/santabarbara-deals.json  (Santa Barbara)
   - deals/centralcoast-deals.json  (the Central Coast)
   - deals/monterey-deals.json  (Monterey & Santa Cruz)
   More California towns will be added to this list as their pages go live.

3. For each file, do what "What the weekly task does" says: re-check every deal already in `deals` against its source (keep and stamp `checked` with today's date, fix, or remove), work the `pending` list (including entries the Sunday health check pulled), drop expired deals, then discover new ones for that town (happy hours, daily food specials, BOGO and early-bird deals, discounted tours and activities) until the town has up to about 25 confirmed deals, aiming for at least 5 per category. Spread your time evenly across the towns.

4. Write each file with "updated" set to today's date (YYYY-MM-DD), deals sorted by category then name. Validate each with python3 -m json.tool. If a town has nothing you could confirm, leave its `deals` list empty rather than guessing.

5. Commit only those files with a message like "Weekly deals (California): sandiego (N), orangecounty (N), losangeles (N), santabarbara (N), centralcoast (N), monterey (N)" and push to main. If the push is rejected because another region's task pushed first, run git pull --rebase and push again. Then run git fetch origin main and confirm origin/main has your commit; if it still fails, say so at the top of your summary with the exact git error.

6. Finish with a short summary: deals per town and category, anything pulled or moved to pending, and any business page that could not be read.
