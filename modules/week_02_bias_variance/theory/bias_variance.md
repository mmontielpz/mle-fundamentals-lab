# Bias–Variance — An Engineering Perspective

Bias–variance is a framework for reasoning about generalization error.
In practice, it is not a formula to compute, but a diagnostic lens
to understand why models fail and what type of corrective action is appropriate.

This note treats bias and variance as observable behaviors in real systems,
not as abstract statistical quantities.

## Generalization error

A model is useful only to the extent that it generalizes beyond its training data.
The central problem in machine learning is not minimizing training error,
but controlling the gap between training and see-un data.

Bias–variance is a framework to reason about this gap.

## Bias

Bias refers to error introduced by overly restrictive assumptions in the model.
A high-bias model cannot represent the underlying data-generating process,
even with unlimited data.

Bias manifests as systematic error.

**Observable signals**
- High error on both training and validation sets
- Residuals exhibit clear structure
- Adding more data does not improve performance

High bias indicates underfitting.
The model class or feature representation is insufficient.

## Variance

Variance refers to error introduced by sensitivity to data fluctuations.
A high-variance model fits noise and idiosyncrasies in the training data
that do not generalize.

Variance manifests as instability.

**Observable signals**
- Low training error but high validation error
- Performance varies significantly across different splits
- Predictions are unstable under small data changes

High variance indicates overfitting.
The model is too flexible relative to the amount of data or signal.

## Bias and variance are not opposites

Bias and variance are not binary states.
Most real systems exhibit both simultaneously.

The goal is not to eliminate bias or variance,
but to reach a regime where both are controlled enough
to support reliable consideration and decision-making.

## Connection to linear regression (Week 01)

Linear regression is typically a high-bias, low-variance model.
Its value lies in the visibility of its failures.

In Week 01, structural residual patterns illustrated a bias-dominated failure mode:
no amount of optimization or additional data could resolve the error.

## Learning curves and validation curves

Bias and variance are not directly observable quantities.
They are inferred through controlled experiments and diagnostic curves.

Two tools are especially useful in practice:
- learning curves
- validation curves

### Learning curves

Learning curves plot training and validation error as a function of training set size.

They answer a critical engineering question:
*Will this model benefit from more data?*

**High bias regime**
- Training error is high
- Validation error is high
- The gap between them is small
- Increasing data size does not reduce error

This indicates an underfitting model.
More data will not help; the representation must change.

### Validation curves

Validation curves plot training and validation error as a function of model complexity
(e.g., polynomial degree, number of parameters, regularization strength).

**Low complexity**
- Both training and validation error are high
- Model cannot capture the signal
- Bias-dominated regime

**High complexity**
- Training error approaches zero
- Validation error increases
- Variance-dominated regime

The optimal operating point lies between these extremes,
where validation error is minimized and the generalization gap is controlled.

## Common misinterpretations

- Low training error does not imply a good model.
- High validation error does not always imply insufficient data.
- Bias and variance are properties of the modeling setup,
  not intrinsic attributes of an algorithm.

A frequent mistake is treating bias–variance as a static trade-off.
In reality, both can change as data, features, and objectives evolve.

## Engineering actions by regime

**Bias-dominated**
- Change model class
- Improve feature representation
- Add relevant signals

**Variance-dominated**
- Increase data volume
- Apply regularization
- Simplify the model
- Improve data quality

**Mixed regimes**
- Combine feature improvements with regularization
- Re-evaluate target definition and noise sources

## Limits of the bias–variance framework

The bias–variance framework is a conceptual tool, not a precise diagnostic formula.
In real systems, bias and variance are not directly measurable and are often entangled
with noise, data quality, and target definition.

Several limitations are worth keeping in mind:

- Bias–variance decompositions rely on assumptions that rarely hold exactly in practice.
- Noise in the data can dominate both bias and variance effects.
- Changes in data distribution can shift a model from one regime to another.
- Evaluation metrics may obscure underlying error structure.

As a result, bias–variance should guide investigation,
not replace empirical validation and domain understanding.

## Summary

Bias–variance is best understood as a diagnostic lens for generalization behavior.
It helps distinguish between errors caused by insufficient model capacity
and errors caused by excessive sensitivity to data fluctuations.

Used correctly, the framework supports informed engineering decisions:
whether to change representation, collect more data, apply regularization,
or reject a modeling approach entirely.

In subsequent modules, these concepts are operationalized through
regularization techniques and controlled experiments.
