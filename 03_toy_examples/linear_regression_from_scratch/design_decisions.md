# Design Decisions — Linear Regression from Scratch

## Scope and Intent
This implementation focuses on **understanding and correctness**, not performance or extensibility.
The goal is to derive, implement, and validate linear regression from first principles.

Out of scope by design:
- Regularization
- Multiple features
- Pipelines or model composition
- Production concerns (latency, memory, serialization)

---

## Why start with scikit-learn as a baseline
Scikit-learn is used as a **numerical oracle**, not as the solution.

Reasons:
- Establish expected coefficients and metrics
- Validate correctness of the closed-form derivation
- Ensure differences later are methodological, not implementation bugs

Once the baseline is validated, it is frozen.

---

## Closed-form solution vs Gradient Descent
The closed-form solution was implemented first because:
- It directly reflects the mathematical derivation
- It guarantees the global optimum for linear regression
- It exposes the dependency on data variance

Limitations:
- Requires computing global statistics
- Does not scale well to high-dimensional data
- Numerically unstable for poorly conditioned matrices

These limitations motivate gradient-based methods in later steps.

---

## Why implement without NumPy
The closed-form solution was implemented using native Python constructs to:
- Make each mathematical operation explicit
- Avoid hiding logic behind vectorized operations
- Strengthen conceptual understanding

This approach is intentionally **not scalable** and is not intended for production use.

---

## Determinism and reproducibility
All experiments:
- Use fixed random seeds
- Use deterministic train/validation splits

This ensures:
- Reproducible results
- Fair comparisons between implementations
- Easier debugging and reasoning

---

## Validation strategy
Correctness is validated by:
- Comparing coefficients and intercepts against scikit-learn
- Comparing validation MSE under identical conditions

Matching results confirm that the implementation is mathematically equivalent.

---

## Known limitations
- Single feature only
- No regularization
- No numerical stability handling beyond variance checks
- Not optimized for speed or memory

These are intentional and aligned with the learning objective.

---

## When this approach breaks
This approach becomes insufficient when:
- The number of features grows
- Data is ill-conditioned
- Online or incremental learning is required
- Performance constraints matter

At that point, vectorized implementations and iterative optimizers are required.
