"""Build the DuckDB database. Owner: D. Assignment Task 4.

Input:  data/interim/     Output: data/processed/*.duckdb
Schema: sql/schema.sql -- read the DDL from that file, do not duplicate it here.

TODO(D):
  [ ] Install and LOAD the spatial extension. Required by the assignment and
      needed for Assignment 2, so verify a spatial query actually runs -- do
      not just assume the extension loaded.
  [ ] Execute sql/schema.sql to create the schema, then load the data.
  [ ] Make the build idempotent: running it twice from scratch gives the same
      database, with no duplicate rows.
  [ ] Keep the DDL in sql/schema.sql. It is a named deliverable and a marker
      will open it; embedding it in Python strings buries it.
  [ ] Verify after loading: row counts against data/interim/, no orphaned
      foreign keys, spatial query returns sensible results.
  [ ] The .duckdb file goes in the submission zip (it is gitignored, so do not
      rely on git to carry it).
"""
