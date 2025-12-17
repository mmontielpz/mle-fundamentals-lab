from typing import List, Tuple


def fit_closed_form(X: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Closed-form solution for simple linear regression (one feature).

    Model:
        y_hat = beta * x + b

    Derived from minimizing:
        J(beta, b) = sum (y_i - (beta * x_i + b))^2

    Returns:
        (beta, b)
    """

    # --- Validations ---
    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    n = len(X)
    if n < 2:
        raise ValueError("At least two data points are required")

    # --- Step 1: compute means ---
    # mean_x = (1/n) * sum(x_i)
    # mean_y = (1/n) * sum(y_i)

    mean_x = sum(X) / n
    mean_y = sum(y) / n

    # --- Step 2: compute numerator and denominator ---
    # beta = sum((x_i - mean_X)(y_i - mean_y)) / sum((x_i - mean_x)^2)

    # corresponds to covariance(x, y)
    numerator = 0.0

    # corresponds to variance(x)
    denominator = 0.0

    for xi, yi in zip(X, y):
        dx = xi - mean_x
        dy = yi - mean_y

        numerator += dx * dy
        denominator += dx * dx

    if denominator == 0.0:
        # All x_i are identical -> no variance -> slope undefined
        raise ValueError("Variance of X is zero; cannot fit linear regression")

    beta = numerator / denominator

    # --- Step 3: compute intercept ---
    # From: mean_y = beta * mean_x + b
    b = mean_y - beta * mean_x

    return beta, b


def predict(X: List[float], coef: float, intercept: float) -> List[float]:
    """
    Generate predictions for simple linear regression.
    """

    if not X:
        raise ValueError("X must not be empty")

    # Implementation will follow
    raise NotImplementedError
