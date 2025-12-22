# Week 02 — Bias–Variance and Generalization

This module introduces the bias–variance framework as an engineering tool to reason about
generalization, model complexity, and expected failure modes.

The focus is not on achieving the best score, but on building reliable intuition and
diagnostic habits that transfer to production systems and interviews.

---

## What this module demonstrates

- How bias and variance manifest empirically through controlled experiments
- Why training error is not a sufficient signal of model quality
- How validation curves reveal underfitting vs overfitting regimes
- How regularization changes the bias–variance trade-off

---

## Module structure

```
theory/
bias_variance.md
regularization_intro.md

notebooks/
01_bias_variance_overview.ipynb

src/
**init**.py

experiments/
**init**.py
```

---

## Suggested reading order

1) `theory/bias_variance.md`  
2) `theory/regularization_intro.md`  
3) `notebooks/01_bias_variance_overview.ipynb`

---

## Scope and intentional limitations

Included by design:
- Synthetic controlled datasets
- Simple models to isolate effects (linear, polynomial, ridge)
- Validation curves and error decomposition intuition

Out of scope:
- Hyperparameter search automation
- Cross-validation pipelines
- Production infra and MLOps

---

## Status

Week 02 is under active development on a feature branch.
