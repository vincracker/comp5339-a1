"""Stage 3 -- Data Augmentation. Owner: D. Assignment Task 3.

Target: >=50% of DC (fast) charger locations enriched with at least one
attribute absent from the TfNSW dataset.

  fetch.py     external source client, writes the local cache
  matching.py  links external records back to TfNSW chargers
"""


def run() -> None:
    """Fetch external charger detail and match it onto the cleaned chargers.

    Reads:  data/interim/ (cleaned chargers), data/external/ (cache)
    Writes: data/external/ (new responses), data/interim/ (matched output)

    TODO(D): read from the data/external/ cache by DEFAULT. A rerun must not
    re-hit the API -- that is what the assignment asks for, and it keeps an
    exhausted quota from blocking the rest of the group. Put the refetch
    behind an explicit opt-in.

    TODO(D): report the match rate against the DC subset every run. It is the
    >=50% target, and B needs the number for the quality report.
    """
    raise NotImplementedError("Stage 3: Data Augmentation -- see src/augmentation/")
