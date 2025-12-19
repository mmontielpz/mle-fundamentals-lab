# Week 01 — Linear Regression from Scratch

This module introduces linear regression as a diagnostic and engineering tool.
The focus is not on achieving high performance, but on understanding assumptions,
failure modes, and system-level implications.

Linear regression is used here as a baseline to reason about data, features,
optimization, and evaluation under real constraints.

---

## Module structure

```

theory/
assumptions.md           # Core assumptions and how they fail in practice
closed_form_vs_gd.md     # Optimization choices and engineering trade-offs
failure_modes.md         # Common production failure patterns

src/
linear_regression.py     # Reference implementation from first principles

notebooks/
01_sklearn_baseline.ipynb        # Baseline comparison against scikit-learn
02_assumption_linearity.ipynb    # Demonstration of linearity violations

experiments/
verify_against_sklearn.py        # Numerical verification and sanity checks

```

---

## Suggested reading order

1) `theory/assumptions.md`  
2) `theory/closed_form_vs_gd.md`  
3) `theory/failure_modes.md`  
4) `notebooks/01_sklearn_baseline.ipynb`  
5) `notebooks/02_assumption_linearity.ipynb`  
6) `experiments/verify_against_sklearn.py`

This order moves from conceptual foundations to empirical validation.

---

## Scope and limitations

This module intentionally focuses on:
- Single-feature linear regression
- Ordinary least squares
- Explicit implementations over abstractions

Out of scope by design:
- Regularization
- Multiple features
- Pipelines or production infrastructure

These topics are introduced in later modules when the limitations become relevant.

---

## Key takeaway

Linear regression is valuable not because it is simple,
but because its failures are visible.

Understanding when and why it fails is a prerequisite
for using more complex models responsibly.

## Execution notes
Notebooks are executed from the module root
(`modules/week_01_linear_regression`).

Local implementations are imported from `src/` as a module,
not installed as a package. This is an intentional choice to
prioritize clarity over distribution mechanics.
