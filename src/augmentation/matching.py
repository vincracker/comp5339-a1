"""Link external records to TfNSW chargers. Owner: D. Assignment Task 3.

Input:  data/interim/ (cleaned chargers) + data/external/ (fetched detail)
Output: data/interim/

This is the technical crux of Task 3: the two datasets share no identifier, so
the link has to be inferred. The assignment asks you to document the strategy
used -- name matching, coordinate matching, address matching, or a combination.

TODO(D):
  [ ] Pick and implement a strategy. Coordinate proximity, name similarity and
      address matching each fail differently; a combination usually beats any
      one alone.
  [ ] Whatever thresholds you choose (distance radius, similarity cutoff),
      keep them in one named place rather than scattered inline, and justify
      the values -- the report has to state them.
  [ ] MEASURE the match rate against the DC subset and track it as you tune.
      This number is the >=50% target -- and B needs it for the quality report.
  [ ] Check the failure modes, not just the hit rate. Two chargers 30m apart at
      one site, or one operator spelled three ways, will silently mismatch.
      Manually verify a sample of matches.
  [ ] If the rate stalls well short of 50%, escalate to the group early --
      there is time to add a second source in week 2, not in week 4.
  [ ] Record ambiguous and failed matches rather than dropping them silently;
      they are report material.
"""
