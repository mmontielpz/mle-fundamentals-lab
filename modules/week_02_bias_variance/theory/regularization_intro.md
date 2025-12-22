# Regularization — Controlling Variance, Not Fixing Models

Regularization is a technique for controlling model variance.
It does not increase the expressive power of a model and cannot correct
structural mis-specification.

This note introduces regularization as an engineering tool to stabilize
generalization behavior, not as a substitute for proper model selection.

## The problem regularization addresses

High-variance models fit noise and idiosyncrasies in the training data.
This results in unstable predictions and poor generalization.

Regularization constrains parameter values to reduce sensitivity
to small variations in the data.

In bias–variance terms, regularization trades a small increase in bias
for a potentially large reduction in variance.

## What regularization is

Regularization modifies the training objective by penalizing model complexity.
For linear models, this typically means adding a penalty on coefficient magnitude.

- L2 regularization (ridge) discourages large coefficients smoothly
- L1 regularization (lasso) promotes sparsity by driving some coefficients to zero

## What regularization is NOT

Regularization does not:
- Make a biased model unbiased
- Recover missing signal
- Fix incorrect features or targets
- Resolve structural assumption violations

If residual diagnostics indicate model mis-specification,
regularization will only mask the problem by shrinking coefficients.

## When regularization helps

Regularization is effective when:
- The model class is appropriate
- Variance dominates the error
- Training and validation error exhibit a large gap

In these cases, regularization can stabilize coefficients,
reduce sensitivity to noise, and improve validation performance.

## When regularization should not be used

Regularization is not appropriate when:
- Both training and validation error are high
- Residuals show strong structure
- The model consistently underfits across data sizes

These signals indicate bias-dominated regimes.
The correct response is to change representation or model class,
not to increase regularization strength.

## Choosing regularization strength

Regularization introduces a hyperparameter that controls the bias–variance trade-off.

In practice, this parameter is selected using validation curves.
The goal is not minimal training error, but stable validation performance
with a controlled generalization gap.

## Connection to upcoming experiments

In the accompanying notebook, regularization effects are demonstrated
using simple models and controlled datasets.

The focus is on observing how validation curves change as regularization
strength varies, and how this relates to bias–variance behavior.

## Summary

Regularization is a variance control mechanism.
It stabilizes models that are already structurally valid
but overly sensitive to data fluctuations.

It is not a remedy for incorrect model assumptions.
Understanding this distinction prevents masking deeper modeling issues
with hyperparameter tuning.
