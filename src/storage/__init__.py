"""Stage 4 -- Data Transformation and Storage. Owner: D. Assignment Task 4.

Loads the processed data into DuckDB with the spatial extension enabled --
required here, and relied on by Assignment 2.

  load.py  builds the database by executing sql/schema.sql
"""


def run() -> None:
    """Build the DuckDB database from the processed data.

    Reads:  data/interim/, sql/schema.sql
    Writes: data/processed/

    TODO(D): make this idempotent -- running it twice from scratch must give
    the same database, with no duplicate rows. Verify the spatial extension
    actually loaded by running a spatial query, rather than assuming it did.
    """
    raise NotImplementedError("Stage 4: Transformation and Storage -- see src/storage/")
