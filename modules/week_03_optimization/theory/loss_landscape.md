# Loss Landscape

Optimization operates over a loss surface defined by the model parameters.

Understanding the geometry of this surface is a prerequisite for reasoning
about convergence, stability, and failure modes of Gradient Descent.

## What a Loss Landscape Represents

A loss landscape maps model parameters to scalar error values.

For linear regression with Mean Squared Error, the landscape is a convex
quadratic surface over the parameter space.

Each point represents:
* A specific set of parameters
* The error induced by those parameters on the dataset

## Geometry Matters

Key geometric properties:
* Convexity guarantees a single global minimum
* Curvature determines sensitivity to updates
* Scale of parameters affects gradient magnitude

Even in convex problems, poor scaling can lead to unstable optimization.

## Implications for Optimization

Gradient Descent does not search intelligently.
It follows the local slope induced by the geometry.

Consequences:
* Flat regions lead to slow convergence
* Steep regions amplify learning rate errors
* Poor feature scaling distorts the landscape

## Engineering Takeaway

Optimization failures are often geometric, not algorithmic.

Before tuning learning rates or changing optimizers,
the loss landscape must be understood and, when possible, reshaped.
