"""Clean the EV charger dataset. Owner: B. Assignment Task 2.

Input:  data/raw/     Output: data/interim/

The assignment names the quality issues it expects you to address: data types,
missing values, duplicate records, inconsistent naming conventions, and
inconsistent charger attributes.

TODO(B):
  [ ] Convert data types; be explicit about latitude/longitude and about any
      column that arrives as text but is really numeric or categorical.
  [ ] Missing values -- decide per column whether to impute, drop or retain,
      and record the reasoning. "Why" matters more than "what" in the report.
  [ ] Duplicates -- decide what makes two rows the same charger. This is
      entangled with the charger identity key, which C and D also depend on --
      settle it with the group rather than unilaterally here.
  [ ] Inconsistent naming -- operator and site names especially. D's matching
      accuracy depends directly on how well this is normalised, so talk to D.
  [ ] Inconsistent charger attributes -- e.g. the same site described
      differently across rows.
  [ ] Define and export the DC (fast charger) subset. C and D both consume it;
      D's >=50% augmentation target is measured against it, so its definition
      needs to be agreed, not assumed.
  [ ] Every cleaning step must be reproducible from data/raw/ -- no manual
      spreadsheet fixes.
"""
