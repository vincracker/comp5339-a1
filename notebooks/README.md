# Notebooks

Notebooks here are for **exploration and report figures**. Pipeline logic lives in `src/`.

That boundary is not stylistic -- it is what keeps four people out of each other's way, and what
keeps the "fully reproducible" requirement true.

## Conventions

**1. Notebooks explore; they do not define.**
The moment something in a notebook becomes load-bearing -- a cleaning rule, a matching threshold, a
join -- it moves into `src/` and the notebook imports it:

```python
from src.integration import cleaning
```

If pipeline behaviour only exists in a notebook cell, it is not reproducible and it is not testable.

**2. One notebook per owner. Never a shared one.**
Name them so ownership is obvious:

```
integration_quality_B.ipynb    # data quality exploration          [B]
integration_spatial_C.ipynb    # visual check of the SA4 join      [C]
augmentation_coverage_D.ipynb  # match rate against the DC subset  [D]
```

Two people in one notebook produces a JSON merge conflict that is genuinely painful to resolve, and
the usual escape is overwriting someone's work. Separate files avoid the problem entirely rather
than managing it.

**3. Fresh kernel, top to bottom, before every commit.**
Restart & Run All. A notebook that only works in your current kernel depends on hidden state -- a
cell run out of order, or a variable from a cell you have since edited. That is the standard way
reproducibility fails silently at marking time.

**4. Figures are saved to files, not left as cell output.**
Write them to `notebooks/figures/` and embed those files in the report:

```python
fig.savefig("notebooks/figures/<name>.png", dpi=200, bbox_inches="tight")
```

Create `notebooks/figures/` the first time you need it -- `savefig` will not create it for you.

Cell outputs are stripped on commit (see below), so a figure that exists only as output will not
survive. Saved figures are committed and are what the report actually references.

## One-time setup -- each member, on their own clone

Notebook outputs are stripped on commit, so diffs stay readable and conflicts stay rare:

```
nbstripout --install
```

This installs a **git filter local to your clone**. It is not carried by cloning the repo, so every
member runs it once themselves. This is the step groups forget -- if someone's commits start showing
thousands of lines of base64 image data in the diff, they skipped it.

TODO(all): confirm each member has run this before real work starts.

## What belongs here

- B: missing values, duplicates, inconsistent naming -- the exploration behind the quality numbers
- C: plotting joined chargers over SA4 boundaries to confirm the join is not silently wrong
- D: augmentation match rate, and inspection of failed or ambiguous matches
- Figures for the report

## What does not

- Data acquisition, cleaning, joining, augmentation or loading logic -- that is `src/`
- Anything the final pipeline run depends on
