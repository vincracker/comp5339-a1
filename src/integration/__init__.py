"""Stage 2 -- Data Integration and Cleaning. Owners: B and C. Assignment Task 2.

Two owners share this package, in separate modules -- keep it that way, so you
are not editing the same file as each other.

  cleaning.py      types, missing values, duplicates, naming, DC subset   [B]
  spatial_join.py  SA4 spatial join                                       [C]
  quality.py       completeness / consistency metrics for the report      [B]
"""


def run() -> None:
    """Clean the raw data, then attach the SA4 region to each charger.

    Reads:  data/raw/
    Writes: data/interim/

    TODO(B, C): order matters -- clean before joining, or the join inherits the
    duplicates and bad coordinates. Agree between you where cleaning ends and
    the join begins, and which of you owns the coordinate columns.
    """
    raise NotImplementedError("Stage 2: Integration and Cleaning -- see src/integration/")
