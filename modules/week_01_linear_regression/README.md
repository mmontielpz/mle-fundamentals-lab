# Week 01 — Linear Regression as an Engineering Baseline

This module establishes linear regression as a **diagnostic baseline**, not as a performance-oriented model.

The goal is to reason about **model validity**, **assumptions**, and **failure modes** from a
Machine Learning Engineering perspective, using first-principles implementations and controlled experiments.

Linear regression is treated as an *instrument* to understand data, features, and error structure,
not as an end solution.

---

## What this module demonstrates

By the end of this week, the following engineering claims are explicitly validated:

* Linear regression exhibits predictable and interpretable behavior when core assumptions hold.
* Violations of the linearity-in-parameters assumption produce **structural error patterns**
  that cannot be resolved through optimization or additional data.
* Residual diagnostics are a **stronger validity signal** than aggregate error metrics.
* Numerical behavior is independent of the solver when the model class is correct.
* A minimal closed-form implementation can be verified against industry-standard libraries.

These conclusions are supported by theory, notebooks, and executable verification scripts.

---

## Module structure

```
theory/
assumptions.md            # Core OLS assumptions and practical diagnostics
closed_form_vs_gd.md      # Solver choices and engineering trade-offs
failure_modes.md          # Common production failure patterns

src/
linear_regression.py      # Closed-form OLS implementation from first principles

notebooks/
01_sklearn_baseline.ipynb         # Reference behavior under ideal assumptions
02_assumption_linearity.ipynb     # Structural violation via residual diagnostics

experiments/
compare_closed_form_with_sklearn.py  # Numerical equivalence verification
```

Each artifact serves a distinct role: **theory defines expectations, notebooks expose behavior,
and experiments validate correctness**.

---

## Suggested reading order

1. `theory/assumptions.md`
2. `theory/closed_form_vs_gd.md`
3. `theory/failure_modes.md`
4. `notebooks/01_sklearn_baseline.ipynb`
5. `notebooks/02_assumption_linearity.ipynb`
6. `experiments/compare_closed_form_with_sklearn.py`

This order progresses from conceptual foundations to empirical evidence and verification.

---

## Scope and intentional limitations

Included by design:

* Single-feature linear regression
* Ordinary Least Squares
* Closed-form solution
* Residual-based diagnostics

Explicitly out of scope:

* Regularization
* Multivariate regression
* Feature engineering
* Pipelines, deployment, or performance optimization

These aspects are introduced in subsequent weeks once the limitations of the baseline
become technically relevant.

---

## Engineering conclusion

Linear regression is valuable not because it is simple,
but because its failures are **observable, explainable, and decisive**.

When residuals exhibit systematic structure, the model is invalid—
regardless of metric values or solver choice.

This week establishes a decision-making baseline:
**when the model class is wrong, tuning is not an option**.

---

## Execution and packaging model

Notebooks are executed from the module root:
`modules/week_01_linear_regression`.

Code under `src/` is treated as a local module and imported directly by
notebooks and experiments. This module is intentionally not packaged as
a distributable library.

This design prioritizes clarity, traceability, and technical reviewability
over distribution mechanics.

---

## Status

Week 01 is considered **complete** and serves as a fixed reference
for subsequent modules.
