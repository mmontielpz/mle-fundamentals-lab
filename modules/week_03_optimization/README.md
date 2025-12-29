# Week 03 – Optimization

This module studies optimization from a Machine Learning Engineering perspective.

The focus is not on tuning optimizers, but on understanding optimization as a
dynamical system with observable failure modes.

## Scope

This week covers:
* Gradient Descent as an iterative numerical process
* Loss surface geometry and its impact on optimization
* Stability, convergence, and divergence behaviors
* Practical diagnostics used in real ML systems

## Non-goals

This module explicitly avoids:
* Blind hyperparameter tuning
* Framework-specific optimizer abstractions
* Treating optimization as a black box
* Shortcut recipes without diagnosis

## Engineering Perspective

Optimization is treated as a controllable system.

Design decisions are justified through:
* Geometry of the loss function
* Update dynamics
* Convergence behavior
* Computational cost

## Deliverables

By the end of this module:
* Gradient Descent is implemented from scratch
* Failure modes are explicitly demonstrated
* GD behavior is compared against closed-form solutions
* Stopping criteria are reasoned, not assumed
