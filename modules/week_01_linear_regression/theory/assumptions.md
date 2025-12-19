# Assumptions — Linear Regression

This note summarizes the key assumptions behind ordinary least squares (OLS) linear regression and what breaks when each assumption is violated. 
The intent is practical: connect assumptions to observable failure modes in real datasets.

## 1) Linearity in parameters

Linear regression assumes the prediction is linear in the parameters:

ŷ = w · x + b

This does not require the real world to be linear. It requires that the relationship can be reasonably approximated by a weighted sum of the chosen features.

What breaks when violated:
- Systematic underfitting even with more data
- Residual patterns that correlate with x (structure in the errors)

Signals to look for:
- Residuals are not randomly scattered; they form curves or segments
- Segment level metrics show consistent bias (over prediction in one region, under prediction in another)

Mitigations:
- Feature engineering (nonlinear transforms, interactions)
- Switch model class if the structure is fundamentally nonlinear

## 2) Independence of errors

OLS assumes errors are independent across observations. In many real settings, observations are correlated:
- time series
- repeated measurements per user or device
- grouped or hierarchical data

What breaks when violated:
- Metrics can look better than they truly are
- Confidence in coefficients is overstated
- Generalization fails when the correlation structure changes

Signals to look for:
- Performance collapses when you split by time or by group
- Residuals show autocorrelation (errors cluster in runs)

Mitigations:
- Use proper splitting strategies (time based, group based)
- Use models that account for correlation or add relevant features

## 3) Zero mean errors

A common assumption is E[ε | x] = 0. In practice, this means the model and features capture the systematic part of the signal, leaving only noise.

What breaks when violated:
- Persistent bias in predictions
- Coefficients compensate for missing variables in unstable ways

Signals to look for:
- Residual mean is not near zero in key segments
- Predictions are consistently shifted up or down

Mitigations:
- Add missing explanatory variables
- Check data leakage and label definition consistency

## 4) Homoscedasticity (constant variance)

OLS often assumes constant error variance across the range of inputs. Many real problems violate this:
- variance grows with magnitude (sales, prices, counts)
- different regimes have different noise levels

What breaks when violated:
- Coefficients can still be unbiased, but uncertainty estimates and diagnostics become misleading
- Outliers dominate learning and evaluation

Signals to look for:
- Residual magnitude increases with x or ŷ
- Error distribution differs strongly by segment

Mitigations:
- Transform the target (log, Box Cox)
- Use robust losses or weighted regression (later modules)

## 5) Normality of errors (optional for prediction)

Normality is not required for making predictions. It matters mainly for classic statistical inference and confidence intervals.

What breaks when violated:
- P values and confidence intervals become unreliable
- Extreme events are under modeled if the true noise is heavy tailed

Signals to look for:
- Heavy tails in residual histograms
- Outlier sensitivity that dominates MSE

Mitigations:
- Robust regression (Huber, quantile regression)
- Evaluate with metrics that reflect tail risk

## 6) No perfect multicollinearity

With multiple features, OLS assumes features are not perfectly collinear. If features are redundant or nearly redundant, coefficients become unstable.

What breaks when violated:
- Large swings in coefficients with small data changes
- Coefficients that are hard to interpret and do not transfer well

Signals to look for:
- High variance in coefficients across splits
- Similar performance but very different learned weights

Mitigations:
- Remove redundant features
- Regularization (ridge) in later modules

## Practical diagnostic checklist

When linear regression underperforms, do not jump to bigger models immediately. First check:

- Residual patterns: is there structure or curvature
- Segments: does performance fail for specific groups
- Outliers: do a few points dominate MSE
- Splits: does time or group splitting collapse performance
- Feature stability: do coefficients vary across runs or folds
