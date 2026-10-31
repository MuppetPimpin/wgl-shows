# wgl-deals: the weekly deals feed for What's Good Local

One file for now: `destin-deals.json`. The Crazy Good Deals page reads it and merges those
deals with the hand-picked deals that live on the WGL server (the `LOCAL_DEALS` list inside the
page). **This feed only adds confirmed deals. It never edits or removes a hand-picked deal.**

| File | Page that reads it | Hand-picked list on the server (read it, never write it) |
|---|---|---|
| `destin-deals.json` | https://whatsgoodlocal.com/crazy-good-deals/ | the `LOCAL_DEALS` list inside that page |

This folder sits in the `wgl-shows` repo next to `football/`, and is refreshed by its own weekly
scheduled task. The live-music and football tasks never touch it.

## The one rule: no source, no listing

Every deal needs a `source`: an https link to the business's own page (menu, happy-hour page,
specials page) or an official post that **states this deal**. If the deal can't be confirmed on
that page, leave it out. A wrong deal is worse than a missing one.

## What the weekly task does

- Re-check every deal already in `deals` against its `source`. Still there → keep it and set
  `checked` to today's date. Changed → fix it to match the source. Gone → remove it.
- Work the `pending` list: for each entry, find the business's own page that states a current
  deal, confirm it, then move it up into `deals` with a real `source` and today's `checked`. If no
  source can be found, leave it in `pending`.
- Drop any deal whose `valid_through` date has passed.
- Never invent a deal, a price, a day or an hour. List only what the source states.

## Finding new deals: discover, then verify

Aggregator and coupon sites — SweetDeals (https://www.sweetdeals.com/fort-walton), Groupon, Viator
and the like — are a **hunting ground, not a source.** They dress offers up as "coupons" that often
do not exist, and their prices rotate week to week. Use them only to find candidate businesses. Then
open the business's **own** site and list the deal exactly as the business states it, with the
business's page as the `source`. If the business has no real offer, drop it.

Groupon/Viator specifics: do not list a rotating Groupon price or promo code. List the operator's
own standing deal, sourced to the operator. The only time a Groupon/Viator listing may be the
`source` is when that operator genuinely sells the offer *only* through that platform — then phrase
it as the operator's offer ("from about $X"), link the operator where possible, and re-check it each
week, because it can change or sell out.

**Known lead sources (hunting grounds — always verify on the provider before listing):**
- SweetDeals — https://www.sweetdeals.com/fort-walton
- SpotDeals — https://spotdeals.app/deals/destin
- Groupon (Destin) — https://www.groupon.com/local/destin-fl
- Valpak (Destin) — https://www.valpak.com/local/destin-fl (coupon network; offers are often real merchant coupons, still verify)
- Restaurant.com (Destin) — https://www.restaurant.com/restaurants-near-destin-fl-us (dining-certificate reseller; the certificate IS the deal, so it may be the source — state the real terms, e.g. "$25 dining certificate for $10, minimum spend applies," and re-check)
- Viator (Destin tours and activities)

Tell-tale sign a site is an aggregator, not the business: the **same stock food/photo repeats across
every listing**, or the "deal" is a generic coupon. Treat those as leads only — the real offer, if
any, lives on the provider's own site, and that is the `source`.

Worked example: SweetDeals lists Urban Air as a coupon. On Urban Air's own site there is no coupon —
there is a standing "Buy 2, Pick 2" offer (https://www.urbanair.com/buy2pick2/). So the deal we list
is "Buy 2, Pick 2," sourced to urbanair.com, never the SweetDeals coupon. When an offer is "valid at
participating locations," confirm the Destin-area location takes part before listing it.

## What to include

- Standing or recurring deals in or near Destin — Destin, Miramar Beach, Sandestin/Baytowne,
  Fort Walton Beach, Okaloosa Island, Niceville, Santa Rosa Beach/30A: happy hours, daily food
  specials, BOGO, early-bird deals, and discounted tours and activities.
- Three categories only: `Food`, `Drinks`, `Adventures`.
- Up to ~40 deals. Prefer variety across towns and categories.

## What to leave out

- One-off events or limited promos whose date has already passed.
- Third-party aggregator prices that move week to week (Groupon, Viator). List the operator's own
  standing deal, with the operator's page as the source, instead of a Groupon price. If you cite a
  range, phrase it "from about $X" and link the operator — never a rotating promo code.
- Anything you can't confirm on the source.
- Hype, or any commentary on a business. Neutral and factual only.

## Partners & click tracking (go.php)

Some businesses here are WGL partners. On each partner deal set `"partner": true` and `"go": "<code>"`,
where `<code>` is that business's offer code in `go.php` (the WGL redirect + scan logger). The Crazy
Good Deals page and the in-room TV both route a partner's button/QR through
`go.php?h=destin&s=deals&o=<code>` (web) or `s=tv` (TV), so go.php logs the click and stamps the
merchant's own UTM. Non-partner deals keep their direct `source` link; the page logs those with a
`sendBeacon` to go.php, so every click still counts on the `s=deals` surface. Keep `source` itself
clean (the real business page) — it's what gets re-verified each week; the `go` code drives tracking.

Carry `partner` and `go` across every weekly refresh (match on the business if a name changes):

| Business | go code |
|---|---|
| Auston's on 98 | `austons98` |
| Jester Mardi Gras Daiquiris | `jester` |
| Pelican Parasail | `pelicanparasail` |
| Pelican Snorkeling Adventure | `pelicansnorkel` |
| Screaming Eagle Dolphin Tours | `screamingeagle` |
| Buccaneer Pirate Cruise | `buccaneer` |
| Southern Star Dolphin Cruise | `southernstar` |
| HarborWalk Adventures | `harborwalk` |
| Sandestin Golf | `sandestingolf` |
| Baytowne on Ice | `baytowne` |
| Wednesday Night Concert Series | `baytowneconcerts` |

New partners: add the business's `go.php` `$DEST` code, then set `partner`/`go` here. Do not invent a
`go` code that isn't in go.php — an unknown code redirects to the go.php default, not the business.

## Writing style

Neutral and factual. American spelling. Do not mention Okaloosa County's text-alert service. Do
not make any claim about paid versus unpaid placement. Keep `deal` short and concrete; keep
`details` to one or two factual sentences.

## Format

```json
{
  "_readme": "What's Good Local weekly deals feed for Destin. Written by the weekly scheduled task; see CLAUDE.md.",
  "updated": "YYYY-MM-DD",
  "deals": [
    {
      "category": "Drinks",
      "name": "AJ's Seafood & Oyster Bar",
      "deal": "$15 dozen raw oysters + $5 house wines, Mon-Fri 3-6 PM",
      "details": "Happy hour Monday to Friday, 3 to 6 PM.",
      "town": "Destin",
      "location": "Destin Harbor · 116 Harbor Blvd",
      "days": "Mon-Fri",
      "hours": "3-6 PM",
      "valid_through": "",
      "featured": false,
      "source": "https://ajsdestin.com/...",
      "checked": "2026-10-30",
      "link": "",
      "phone": ""
    }
  ],
  "pending": [
    { "name": "The Back Porch", "note": "last-known: happy hour 3-5 PM daily. Confirm current deal + find source." }
  ]
}
```

- **Required:** `category`, `name`, `deal`, `town`, `source`, `checked`. The page drops a deal
  missing any of these.
- `category` must be exactly `Food`, `Drinks`, or `Adventures`.
- `valid_through`: blank = evergreen (happy hours never expire). A date (`YYYY-MM-DD`) makes the
  page auto-hide the deal the day after.
- `featured`: `true` floats a deal to the top of its category. This is a business decision set
  here, not a judgment about the deal.
- `location`, `days`, `hours`, `link` (booking/menu button), `phone` are optional.
- `partner` (`true`) and `go` (the go.php offer code) are optional — set both only for the confirmed
  partners in the table above. They drive the go.php click tracking; omit for everyone else.
- Every link starts with `https://`. Sort `deals` by category then name. Keep the JSON valid
  (check it with `python3 -m json.tool`).
