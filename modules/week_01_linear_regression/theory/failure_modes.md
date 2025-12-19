# Failure Modes — Linear Regression in Practice

Linear regression rarely fails because the optimization did not converge.
It fails because assumptions are violated, data changes, or the system is misused.

This note documents common failure modes observed in real systems and how they manifest operationally.

## Silent underfitting

**Description**  
The model converges cleanly, metrics look stable, but performance is consistently mediocre.

**Why it happens**
- The signal is non-linear
- Features are weak or incomplete
- Important interactions are missing

**Operational symptoms**
- Residuals show structure but dashboards look “healthy”
- Metrics improve slowly or plateau early
- Adding more data does not help

**Mitigation**
- Residual analysis by segment
- Simple non-linear baselines for comparison
- Revisit feature definitions before changing model class

## Data leakage masking true performance

**Description**  
The model appears strong during validation but fails in real usage.

**Why it happens**
- Leakage from future information
- Improper splitting (random instead of time or group based)
- Target-derived features

**Operational symptoms**
- Sudden performance collapse after deployment
- Training metrics significantly better than production metrics

**Mitigation**
- Enforce split strategies aligned with deployment reality
- Validate features for temporal or logical leakage
- Keep feature generation reproducible and auditable

## Outlier dominance

**Description**  
A small number of points dominate training and evaluation.

**Why it happens**
- MSE penalizes large errors aggressively
- Heavy-tailed noise distributions
- Rare but extreme events

**Operational symptoms**
- Model behavior driven by a few samples
- High variance across retraining runs
- Instability when outliers appear or disappear

**Mitigation**
- Inspect error distributions, not just averages
- Robust losses or target transforms
- Segment-specific evaluation

## Feature drift and coefficient instability

**Description**  
Model performance degrades gradually without obvious code changes.

**Why it happens**
- Feature distributions shift over time
- Coefficients compensate for drift in unstable ways
- Linear models extrapolate poorly outside observed ranges

**Operational symptoms**
- Slowly increasing error over time
- Coefficients change significantly between retraining runs
- Segment-level failures emerge first

**Mitigation**
- Monitor feature distributions
- Track coefficient stability
- Retrain with controlled windows and diagnostics

## Misinterpreting coefficients as causal

**Description**  
Coefficients are treated as causal signals when they are only correlational.

**Why it happens**
- OLS coefficients are easy to inspect
- Interpretability is over-trusted
- Confounders are ignored

**Operational symptoms**
- Business decisions based directly on coefficients
- Unexpected regressions when context changes

**Mitigation**
- Treat coefficients as descriptive, not causal
- Validate insights with controlled experiments when possible
- Communicate limitations explicitly

## When linear regression is the wrong tool

Linear regression is not a fallback model.
It is inappropriate when:
- The signal is fundamentally non-linear and high-dimensional
- Interactions dominate behavior
- Latent structure cannot be captured with engineered features

In these cases, larger models may be justified.
The key is knowing *why* a model fails before replacing it.

## Summary

Linear regression is valuable because its failure modes are visible.
Understanding these modes allows teams to diagnose data, features,
and system design issues early, before complexity hides them.
