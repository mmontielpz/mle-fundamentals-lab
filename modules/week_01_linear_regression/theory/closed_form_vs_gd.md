# Closed-Form Solution vs Gradient Descent

Linear regression admits two common training approaches:
a closed-form analytical solution and iterative optimization via gradient descent.
Both solve the same objective, but their engineering implications differ significantly.

This note focuses on when each approach is appropriate and what trade-offs matter in practice.

## Problem setup

Given a dataset with feature vector x and target y, linear regression minimizes:

J(w, b) = (1 / n) Σ (yᵢ − (w · xᵢ + b))²

The objective is convex. There is a single global minimum.

## Closed-form solution

For simple linear regression (one feature), parameters can be computed analytically:

w = cov(x, y) / var(x)  
b = ȳ − w · x̄

For multiple features, the solution generalizes to:

w = (Xᵀ X)⁻¹ Xᵀ y

### Why it is attractive

- Exact solution in one step
- No learning rate tuning
- Deterministic outcome
- Useful as a correctness reference

### Practical limitations

- Requires computing global statistics
- Matrix inversion scales poorly with feature count
- Numerically unstable when Xᵀ X is ill-conditioned
- Not suitable for streaming or incremental data

In real systems, these limitations dominate quickly as dimensionality grows.

## Gradient descent

Gradient descent minimizes the same objective iteratively by following the gradient:

w ← w − α ∂J/∂w  
b ← b − α ∂J/∂b

### Why it is preferred in practice

- Scales to large datasets
- Avoids matrix inversion
- Works with mini-batches and streaming data
- Extends naturally to non-linear models

### Trade-offs introduced

- Requires learning rate selection
- Convergence depends on feature scaling
- Introduces optimization diagnostics as a concern

Gradient descent does not change the model’s expressive power.
It changes how efficiently and stably the same optimum is reached,
assuming the model class is valid.

## Numerical stability and conditioning

The choice between closed-form and gradient-based methods is often dictated by conditioning.

When features have vastly different scales or are highly correlated:
- Closed-form solutions amplify numerical errors
- Gradient descent can still converge if features are scaled

This is why feature scaling is not an optimization detail, but a stability requirement.

## What optimization cannot fix

Closed-form solutions and gradient descent solve the same objective.
If the linear model is mis-specified, both methods converge to an
invalid solution with different numerical paths.

Optimization affects convergence behavior, not model validity.
Structural errors caused by violated assumptions will persist
regardless of solver choice.

## Engineering perspective

From an engineering standpoint:

- Closed-form solutions are excellent for:
  - sanity checks
  - toy examples
  - correctness validation

- Gradient-based methods are preferred for:
  - large-scale data
  - evolving datasets
  - production systems

In practice, teams often compute the closed-form solution once as a reference
and then rely on gradient-based methods for training and iteration.

## Connection to this module

In this module:
- The closed-form solution is implemented explicitly to expose assumptions
- Gradient descent is introduced to highlight scalability and stability trade-offs

Both implementations solve the same problem.
The difference lies in operational constraints, not modeling power.
Neither approach can compensate for a structurally invalid model.
