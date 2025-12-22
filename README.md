# MLE Fundamentals Lab

A public, module-based lab to build and demonstrate Machine Learning Engineering
fundamentals from first principles.

This repository is structured as a sequence of self-contained technical modules,
each focused on a single core concept and treated as an engineering problem:
with explicit assumptions, controlled experiments, and verifiable conclusions.

The goal is not to collect models, but to develop diagnostic reasoning,
decision-making criteria, and technical rigor expected of senior MLE roles.

---

## Repository structure

```
modules/
week_01_linear_regression/
week_02_bias_variance/
```

Each module follows a consistent internal structure:

```
theory/        # Assumptions, limits, and failure modes
notebooks/     # Empirical diagnostics and visualizations
experiments/   # Reproducible verification scripts
src/           # Minimal reference implementations (when applicable)
```

Modules are designed to be:
- Conceptually scoped
- Independently runnable
- Closed once validated
- Referencable via tags

---

## What this repository emphasizes

This lab prioritizes:

- Understanding over tooling
- Explicit implementations over black-box usage
- Diagnostics over metric chasing
- Model validity over optimization tricks
- Reproducibility over exploration

Each module answers a specific engineering question
and establishes criteria for when a modeling approach should be accepted,
modified, or rejected.

---

## Current modules

- **Week 01 — Linear Regression**  
  Baselines, assumptions, residual diagnostics, and structural failure modes.

- **Week 02 — Bias–Variance and Generalization**  
  Empirical bias–variance behavior, validation curves, and controlled
  regularization experiments.

Each completed module is treated as immutable
and tagged once conceptually and technically closed.

---

## Scope and progression

This repository intentionally delays:

- Hyperparameter search automation
- Cross-validation pipelines
- MLOps and deployment infrastructure
- Performance optimization

These topics are introduced only after the underlying diagnostic
and modeling foundations are established.

---

## Cadence

Each module:

1) Defines the problem and assumptions
2) Builds minimal reference implementations
3) Makes behavior observable through experiments
4) Verifies conclusions with reproducible scripts
5) Is documented and closed before moving on

Selected modules are summarized and shared externally
as part of a continuous learning and technical documentation process.
```
