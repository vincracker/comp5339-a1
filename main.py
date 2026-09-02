"""Run the full pipeline, end to end.

    acquisition -> integration -> augmentation -> storage

TODO(all): wire the four stages together. Each exposes run(); call them in the
order above. Keep this thin -- it orchestrates, it does not do the work.

The reproducibility requirement is judged on this path: a clean clone plus a
clean virtual environment plus this one command must produce the .duckdb, with
no manual download and no hand-edited files.

TODO(all): decide how a partial run is invoked. Re-running acquisition and
augmentation on every change is painful, so during development you will want to
run stages individually -- via arguments here, or by calling the stage's run()
directly. Whichever you choose, document it in the README.
"""


def main() -> None:
    # TODO(all): call the four stage run() functions in order.
    raise NotImplementedError("Pipeline not wired up yet -- see the TODOs above.")


if __name__ == "__main__":
    main()
