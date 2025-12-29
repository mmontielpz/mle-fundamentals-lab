# Gradient Descent Dynamics

Gradient Descent is an iterative numerical procedure that updates model
parameters by following the local gradient of the loss surface.

It is not a learning mechanism.
It is a dynamical system whose behavior depends on its update rule and controls.

## Update Rule as a System

At each iteration:

θ_{t+1} = θ_t − α ∇L(θ_t)

Where:
* θ represents model parameters
* ∇L is the gradient of the loss
* α is the learning rate

This defines a discrete-time dynamical system.

## Role of the Learning Rate

The learning rate controls step size, not intelligence.

Its interaction with:
* Gradient magnitude
* Curvature of the loss surface
* Feature scaling

determines whether the system is:
* Stable
* Oscillatory
* Divergent

## Stability Intuition

Small learning rates:
* Stable
* Slow convergence
* High computational cost

Large learning rates:
* Faster movement
* Risk of overshooting
* Oscillations or divergence

There is no universally correct value.
Stability is problem-dependent.

## Gradient Magnitude and Scaling

The gradient is sensitive to:
* Feature scale
* Parameter initialization
* Dataset size

Unscaled features distort the update dynamics, often leading to unstable or
inefficient optimization.

## Engineering Takeaway

Gradient Descent behavior emerges from interaction between:
* Geometry of the loss surface
* Update rule
* Learning rate
* Data scaling

Optimization problems are rarely solved by changing optimizers.
They are solved by understanding and controlling the dynamics.
