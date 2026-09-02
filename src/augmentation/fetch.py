"""Fetch charger detail from an external source. Owner: D. Assignment Task 3.

Output: data/external/ (cached CSV, committed to git)

Candidate sources -- the assignment allows any of:
  - the EV charger operator's own website (scraping)
  - Open Charge Map
  - Google Maps
  - another open Web API

Candidate attributes: plug types, pricing, operator details, number of bays.

TODO(D):
  [ ] Choose the source. Weigh coverage of NSW DC chargers against effort and
      rate limits -- the >=50% target is the binding constraint, so estimate
      likely coverage on a sample BEFORE committing to a source.
  [ ] Cache every response to data/external/ and read from cache on re-runs.
      The assignment asks for this explicitly, and it means an exhausted API
      quota does not block the other three members.
  [ ] Respect rate limits: throttle, back off on failure, resume without
      re-fetching what you already have.
  [ ] If scraping, check the site's terms and robots.txt first, and be gentle.
  [ ] Document the access method and any API parameters used -- the report has
      to identify the source and describe how you accessed it.
  [ ] Credentials from the environment only (see .env.example).
"""
