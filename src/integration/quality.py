"""Quantify data completeness and consistency. Owner: B. Assignment Task 5.

Feeds the report section "Data Cleaning and Quality Assessment". The assignment
asks you to discuss completeness and consistency of BOTH the original and the
augmented datasets -- so this runs twice: once on raw, once after augmentation.
That means coordinating with D on when the augmented data is ready.

TODO(B):
  [ ] Produce counts and rates, not adjectives. "3.2% of rows lacked an operator
      name (412/12,908)" is markable; "the data was fairly clean" is not.
  [ ] Report before/after figures for each cleaning step, so the report can show
      what the cleaning actually achieved.
  [ ] Emit results as a file under data/interim/ rather than printing, so
      the numbers in the report are traceable to a rerunnable artefact and do
      not have to be retyped by hand.
  [ ] Cover the augmented dataset too -- including D's match rate against the
      >=50% DC target.
"""
