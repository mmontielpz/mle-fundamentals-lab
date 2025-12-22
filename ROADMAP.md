# Weekly Roadmap

This roadmap outlines the progressive construction of Machine Learning Engineering
fundamentals through self-contained weekly modules.

Each week introduces one core concept, treats it as an engineering problem,
and is closed once assumptions, diagnostics, and verification artifacts are complete.

---

## Week 01 — Linear Regression Foundations

Focus:
- Linear regression as a diagnostic baseline
- Assumptions, residual analysis, and structural failure modes

Artifacts:
- Theory notes on OLS assumptions and failure patterns
- From-scratch reference implementation
- Sklearn baseline notebook with frozen invariants
- Controlled experiments verifying numerical correctness

Status: Complete

---

## Week 02 — Bias–Variance and Generalization

Focus:
- Empirical bias–variance behavior
- Model complexity and validation diagnostics
- Regularization as a variance control mechanism

Artifacts:
- Theory notes on bias–variance trade-off and regularization
- Notebooks demonstrating overfitting and regularization effects
- Reproducible experiment comparing regularized vs unregularized models

Status: Complete

---

## Week 03 — Optimization and Gradient Descent Dynamics

Focus:
- Optimization as a separate concern from modeling
- Gradient descent behavior, convergence, and instability
- Effects of learning rate, scaling, and initialization

Planned artifacts:
- Theory notes on optimization vs closed-form solutions
- From-scratch gradient descent implementation
- Experiments illustrating convergence and divergence regimes
- Comparison with analytical solutions when available

Status: Planned

---

## Week 04 — Feature Scaling, Conditioning, and Numerical Stability

Focus:
- Conditioning and its impact on optimization
- Feature scaling as a stability requirement, not a preprocessing detail
- Interaction between scaling, regularization, and convergence

Planned artifacts:
- Theory notes on conditioning and numerical issues
- Experiments showing failure without scaling
- Diagnostic criteria for detecting instability

Status: Planned

---

## Week 05 — System Perspective: Batch vs Online Learning

Focus:
- Modeling assumptions under different system constraints
- Batch vs incremental updates
- Latency, cost, and retraining trade-offs

Planned artifacts:
- Architecture notes
- Conceptual system diagrams
- Failure modes under data drift and delayed feedback

Status: Planned

---

## Notes

Later weeks will introduce:
- Cross-validation and model selection
- Hyperparameter tuning as an engineering process
- Monitoring and drift detection
- Production considerations (MLOps) only when diagnostically justified
