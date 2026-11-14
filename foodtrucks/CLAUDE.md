# foodtrucks/ — the Best Food Trucks feed

`trucks.json` is read by the Best Food Trucks pages on whatsgoodlocal.com (one shared Elementor block,
one page per area: destin, fwb, miramar, santarosa, navarre, pensacola, pcb). The page has a built-in
copy, so a bad edit here never blanks the page, but keep the JSON valid (`python3 -m json.tool`).

Updated by hand for now (no scheduled task yet).

## Rules
- **No source, no listing.** Every truck and hub has a `src` https link that shows where it parks.
- Only list trucks with a real spot: a fixed address, a truck park, or a regular weekly stop.
  Trucks that only post day-of on Facebook stay out until they check in with us.
- `h` (hours) is 7 entries, Sunday first: `"1100-2100"` = open those times (Central),
  `"*"` = there that day but times vary / until sold out, `""` = closed. Leave `h` out if unknown.
- `type`: `parked`, `rotates`, or `boat`. Optional: `phone` (10 digits), `order` (their own
  ordering page: Toast, Square, DoorDash), `web`, `fb`, `note`, `drive`, `tags`
  (tacos, bbq, burgers, seafood, southern, global, sweet).
- `near`: truck parks in another area worth the drive, as `area:hubId`.
- Neutral, factual wording. No hype, no commentary on the trucks.
