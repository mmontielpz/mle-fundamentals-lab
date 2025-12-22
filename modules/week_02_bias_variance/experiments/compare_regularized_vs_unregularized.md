# Experiment — Regularized vs Unregularized High-Variance Model

## Objective

Verify that regularization improves generalization in a variance-dominated regime
without changing the underlying model class or data-generating process.

This experiment isolates the effect of regularization by comparing two models
that differ only in the presence of an L2 penalty.

---

## Hypothesis

For a structurally valid but high-variance model:

- An unregularized model will achieve low training error but poor validation performance.
- A regularized model will exhibit higher training error but improved validation performance.
- Regularization will not change the model’s expressive power or correct mis-specification.

---

## Experimental setup

### Data
- Synthetic non-linear data
- Same data-generating process as used in Week 02 notebooks
- Fixed random seed for reproducibility

### Model structure
- Polynomial regression with a fixed high degree (variance-dominated regime)
- Feature scaling applied to avoid numerical instability

### Models compared
1. Unregularized linear regression
2. Ridge regression with fixed regularization strength

### Invariants
- Same dataset
- Same train/validation split
- Same feature transformation
- Same evaluation metric (MSE)

---

## Evaluation

The following metrics are reported for each model:
- Training mean squared error
- Validation mean squared error

No hyperparameter tuning or model selection is performed.

---

## Expected outcome

- The unregularized model exhibits a large generalization gap.
- The regularized model reduces validation error at the cost of increased training error.
- The result supports the interpretation of regularization as a variance control mechanism.

---

## Out of scope

- Searching for optimal regularization strength
- Cross-validation
- Model architecture changes
- Performance optimization

---

## Conclusion criteria

If regularization does not improve validation error under this setup,
the issue is likely data-related or indicative of deeper model mis-specification.
