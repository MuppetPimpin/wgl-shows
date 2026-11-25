Run the weekly site health check for What's Good Local and BeachSmart and report to Eddy. This is READ-ONLY with ONE exception (step 7, the deals auto-pull): never edit any page, file, server, repo or account except as step 7 allows. Otherwise only look and report.

1. Load the page lists:
   - https://whatsgoodlocal.com/sitemap_index.xml and every sitemap it lists
   - https://beachsmart.app/sitemap.xml
   - https://whatsgoodlocal.com/beachsmart-sitemap.xml (every town page: beach conditions, things to do, live music, where to eat, crazy good deals)
   - These pages too, even if they're not in a sitemap: https://whatsgoodlocal.com/beach-conditions/, https://whatsgoodlocal.com/pensacola/live-music/, https://whatsgoodlocal.com/santa-rosa-beach-conditions/, https://whatsgoodlocal.com/grayton-beach-conditions/, https://whatsgoodlocal.com/seaside-beach-conditions/, https://whatsgoodlocal.com/seagrove-beach-conditions/, https://whatsgoodlocal.com/rosemary-beach-conditions/, https://whatsgoodlocal.com/panama-city-beach/beach-conditions/, https://whatsgoodlocal.com/panama-city-beach/live-music/, https://whatsgoodlocal.com/crazy-good-deals/, https://tampa.whatsgoodlocal.com/beach-conditions/, https://tampa.whatsgoodlocal.com/live-music/, https://gulfshores.whatsgoodlocal.com/beach-conditions/, https://orangebeach.whatsgoodlocal.com/beach-conditions/, https://beachsmart.app/, https://beachsmart.app/properties/, https://beachsmart.app/privacy/
   Use curl from the shell (with a normal browser User-Agent) where it works, and WebFetch where it doesn't. If a page returns a bot-check page instead of the real page, say so rather than counting it as broken. Space requests a second apart.

2. For every page: record the HTTP status (anything not 200 after redirects is a problem) and load time if it's over 8 seconds.

3. For every page: collect image URLs (img src, srcset first entry, CSS background url(...), og:image). Resolve relative paths against the page URL, de-duplicate, and check each once. Any image that doesn't return 200 is broken. Also flag any image hosted on imgur.

4. Check https://whatsgoodlocal.com/robots.txt, https://beachsmart.app/robots.txt and the sitemaps return 200, and that robots.txt doesn't block the whole site.

5. Check each page for: a missing <title>, a missing meta description, a noindex tag on a page that's in a sitemap, and duplicate titles across pages.

6. Check every auto-updating feed in this repo: every *.json file at the repo root, every deals/*-deals.json, plus football/schedule.json, ufc/schedule.json, wine/events.json, guide/events.json, boardwalk/events.json, casinos/events.json and foodtrucks/trucks.json. Flag any file whose "updated" date is more than 8 days old or that isn't valid JSON. List live music files with 0 shows and deals files with 0 deals by town, in two groups: towns in season, and off-season towns where empty is expected in winter (Outer Banks, Virginia Beach, Ocean City MD, Nature Coast, Forgotten Coast, Crystal Coast, Chicago, New York).
   Also check https://whatsgoodlocal.com/space-coast/rocket-launches/launches.json: flag it if it isn't valid JSON or its "updated" timestamp is more than 12 hours old.

7. DEALS AUTO-PULL (the only write this task may make). Read deals/CLAUDE.md, section "Sunday health check (auto-pull)". For every entry in the "deals" list of deals/destin-deals.json:
   - open its "source" with curl (browser User-Agent, follow redirects, retry once after 10 seconds). If it returns 404 or 410, or fails to load on both tries, it is broken. A bot-check or 403 page is NOT broken: leave it and just mention it.
   - "valid_through" set and already past = expired.
   - "checked" more than 14 days before today = stale.
   Move each broken, expired or stale deal out of "deals" into "pending", unchanged except for two added fields: "pending_reason" ("source link broken (404)", "expired", or "not checked since YYYY-MM-DD") and "pulled" (today's date). Do not edit, rewrite or delete any deal, never touch "partner" or "go", and never touch any other file. Validate with python3 -m json.tool deals/destin-deals.json. If anything moved, commit only deals/destin-deals.json with a message like "Health check: pulled 3 deals to pending (2 broken links, 1 stale)", end the message with
   Co-Authored-By: Claude <noreply@anthropic.com>
   and push to main; then run git fetch origin main and confirm origin/main has the commit (retry once with pull --rebase if rejected). If nothing needed pulling, change nothing.
   Also open the hand-picked LOCAL_DEALS list inside https://whatsgoodlocal.com/crazy-good-deals/ and test each "source" and "link" the same way. Those live on the server and must NOT be edited: just list any broken ones in the report.

8. Finish with a short report for Eddy, worst problems first:
   - BROKEN: pages down, broken images (page URL and image URL), robots/sitemap problems
   - DEALS PULLED: each deal moved to pending, with its reason, and whether the push landed; plus any broken link in the hand-picked deals on the page
   - CHECK: slow pages, missing titles or descriptions, noindex conflicts, duplicate titles, stale feeds, empty town feeds, a stale launch schedule
   - A one-line count: pages checked, images checked, deals checked
   If everything passes, say "All clear" with the counts. Keep wording neutral. Give exact URLs so each fix is quick. If a site won't load at all, say so plainly instead of guessing. Never mention Okaloosa County's text-alert service.
