"""Retrieve ABS ASGS SA4 digital boundary files. Owner: A. Assignment Task 1.

Source: ASGS Edition 4 (July 2026 - June 2031), digital boundary files.
  https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-4-july-2026-june-2031/access-and-downloads/digital-boundary-files

Output: data/raw/

TODO(A):
  [ ] Identify the direct download URL for the SA4 boundary archive. Confirm
      it is the SA4 (regional) level, and Edition 4 -- not an earlier edition.
  [ ] Download and unpack programmatically. A shapefile is a set of sidecar
      files (.shp/.shx/.dbf/.prj/...); they must be kept together.
  [ ] Note the archive's CRS from the .prj and pass it to C -- the join is
      silently wrong if the two layers disagree on CRS.
  [ ] This file is large. Fetching it by script rather than committing it keeps
      the repo manageable AND evidences the "no manual downloading" requirement.
  [ ] Make re-runs cheap: skip the download if the file is already present and
      intact, so B/C/D are not re-downloading it all day.
"""
