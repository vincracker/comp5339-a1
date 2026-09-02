"""Spatially join chargers to SA4 regions. Owner: C. Assignment Task 2.

Input:  data/interim/ (cleaned chargers) + data/raw/ (SA4 boundaries)
Output: data/interim/

Goal: add a field to each charger for the SA4 region containing it.

TODO(C):
  [ ] Decide GeoPandas vs DuckDB spatial, and justify it in the report. Worth
      weighing: DuckDB's spatial extension has to be installed anyway for
      Task 4 and Assignment 2, which makes doing the join there defensible --
      but GeoPandas may be faster to iterate on. Either is fine; the marks are
      in the justification, so keep a note of why you chose what you chose.
  [ ] CRS handling. Confirm the charger coordinates' CRS and the SA4 file's
      CRS (A reports this from the .prj) and reproject so both match
      before joining. A silent CRS mismatch produces a plausible-looking join
      that is entirely wrong -- this is the most common way this task fails.
  [ ] Validate the result. Every NSW charger should land in exactly one SA4.
      Investigate: chargers matching zero regions (offshore, bad coordinates,
      outside NSW) and any matching more than one (boundary cases).
  [ ] Report the unmatched count and explain what you did about it -- this is
      good material for "Challenges and Limitations", not something to hide.
  [ ] Sanity-check a handful of known locations by hand against a map.
"""
