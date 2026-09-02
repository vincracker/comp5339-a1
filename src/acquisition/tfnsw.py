"""Retrieve NSW EV charger locations. Owner: A. Assignment Task 1.

Source -- either one is acceptable:
  - TfNSW Open Data: https://opendata.transport.nsw.gov.au/data/dataset/ev-charging-locations
    (requires a free account)
  - data.gov.au: https://data.gov.au/data/dataset/nsw-2-ev-charging-locations

Output: data/raw/

TODO(A):
  [ ] Register for the TfNSW account early -- approval delay is pure schedule
      loss with no workaround. Do this before anything else.
  [ ] Decide TfNSW vs data.gov.au, and keep a note of why -- the report asks
      you to explain your retrieval method.
  [ ] Pin the DECEMBER 2025 version specifically. The assignment asks for that
      release, not merely "the latest" -- if the endpoint serves latest-by-
      default, work out how to request the dated one.
  [ ] Read credentials from the environment (see .env.example). Never hardcode
      a key: the source package is a submitted deliverable.
  [ ] Write the raw response to data/raw/ unmodified, before any parsing.
  [ ] Record the retrieval timestamp and the resolved source URL so the report
      can state exactly what was downloaded and when.
  [ ] Handle failure explicitly -- auth rejection, rate limit, network error.
"""
