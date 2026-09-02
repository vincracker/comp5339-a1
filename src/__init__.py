"""COMP5339 Assignment 1 -- EV charger data integration and augmentation.

Four stages, one per assignment task, run in order:

    1. acquisition   TfNSW chargers + ABS ASGS SA4 boundaries      [A]
    2. integration   cleaning, quality metrics, SA4 spatial join   [B, C]
    3. augmentation  external attributes for DC chargers           [D]
    4. storage       DuckDB build with the spatial extension       [D]

Each package exposes a single run() entry point, so a stage can be invoked on
its own while developing (acquisition and augmentation are slow) or driven end
to end from main.py.

Data flows through data/ and never between stages in memory -- see the .gitkeep
in each directory for what belongs where. Agree the columns, types and grain of
each handoff, and the charger identity key, before writing stage logic; the
stages will not compose otherwise.
"""
