"""Stage 1 -- Data Acquisition. Owner: A. Assignment Task 1.

Retrieval must be fully automated: no manual downloading, no clicking through a
browser. Outputs land in data/raw/ and are never edited by hand afterwards.

  tfnsw.py     EV charger locations (December 2025 release)
  abs_asgs.py  SA4 digital boundary shapefile (ASGS Edition 4)
"""


def run() -> None:
    """Fetch both source datasets into data/raw/.

    Reads:  nothing (network + credentials from .env)
    Writes: data/raw/

    TODO(A): call the tfnsw and abs_asgs retrievals. Skip work already done --
    this stage is slow, and B/C/D will run it repeatedly. Decide what "already
    done" means (file present? size check? checksum?) and say so in the README.
    """
    raise NotImplementedError("Stage 1: Data Acquisition -- see src/acquisition/")
