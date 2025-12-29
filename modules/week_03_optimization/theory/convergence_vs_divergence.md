# Convergence vs Divergence

Gradient Descent behavior is evaluated through its observable trajectories,
not through intent or configuration alone.

This document classifies the main behaviors encountered during optimization
and links them to practical engineering causes.

## Stable Convergence

Characteristics:
* Monotonic decrease of loss
* Gradual parameter stabilization
* Bounded gradients

Common causes:
* Appropriate learning rate
* Well-scaled features
* Convex or well-conditioned loss surface

Engineering interpretation:
The system is numerically stable and progressing toward an optimum.

## Oscillation

Characteristics:
* Loss fluctuates around a region
* Parameters overshoot the optimum
* No clear downward trend

Common causes:
* Learning rate too high
* High curvature in the loss surface
* Poor feature scaling

Engineering interpretation:
The system is unstable but bounded.
Control parameters need adjustment.

## Divergence

Characteristics:
* Exploding loss values
* Parameter norms grow without bound
* NaNs or infinities appear

Common causes:
* Excessive learning rate
* Extreme curvature or ill-conditioned features
* Numerical instability

Engineering interpretation:
The optimization process is broken and must be halted.

## Stagnation

Characteristics:
* Loss plateaus early
* Minimal parameter updates
* Slow or no improvement

Common causes:
* Learning rate too low
* Flat regions in the loss surface
* Poor initialization

Engineering interpretation:
The system is stable but inefficient.

## Engineering Takeaway

Optimization must be diagnosed through behavior.

Loss curves, gradient norms, and parameter trajectories are primary signals.
Hyperparameters are secondary controls, not explanations.
