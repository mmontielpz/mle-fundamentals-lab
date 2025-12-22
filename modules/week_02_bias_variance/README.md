# Week 02 — Bias–Variance and Generalization

This module develops the bias–variance framework as an engineering tool
to reason about generalization, model complexity, and expected failure modes.

The focus is not on achieving the best score, but on building reliable intuition,
diagnostic discipline, and decision-making criteria that transfer to
production systems and technical interviews.

---

## What this module demonstrates

- How bias and variance manifest empirically through controlled experiments
- Why training error alone is an insufficient indicator of model quality
- How validation curves expose underfitting and overfitting regimes
- How regularization controls variance without changing model class
- How empirical observations can be verified with reproducible experiments

---

## Module structure

```
theory/
bias_variance.md
regularization_intro.md

notebooks/
01_bias_variance_overview.ipynb
02_regularization_effects.ipynb

experiments/
compare_regularized_vs_unregularized.md
compare_regularized_vs_unregularized.py
```

Each artifact serves a distinct role:
- theory defines concepts and limits
- notebooks make phenomena observable
- experiments verify behavior under controlled invariants

---

## Suggested reading order

1) `theory/bias_variance.md`  
2) `theory/regularization_intro.md`  
3) `notebooks/01_bias_variance_overview.ipynb`  
4) `notebooks/02_regularization_effects.ipynb`  
5) `experiments/compare_regularized_vs_unregularized.py`

This sequence moves from conceptual framing to empirical observation
and finally to reproducible verification.

---

## Scope and intentional limitations

Included by design:
- Synthetic, controlled datasets
- Simple models to isolate bias–variance effects
- Fixed data-generating processes
- Diagnostics via training and validation error
- Explicit regularization comparison

Out of scope:
- Hyperparameter search automation
- Cross-validation pipelines
- Production infrastructure and MLOps
- Performance optimization

These topics are addressed in later modules once diagnostic foundations are established.

---

## Engineering takeaway

Bias–variance is not a formula to compute, but a lens to interpret error behavior.

Regularization is a variance control mechanism.
It improves generalization only when the underlying model class is appropriate
and cannot correct structural mis-specification.

This module establishes criteria for deciding whether to:
- change model complexity,
- introduce regularization,
- collect more data,
- or reject a modeling approach entirely.

---

## Status

Week 02 is considered **complete** and serves as a reference module
for subsequent work on optimization and model selection.
