from typing import List, Tuple


def fit_closed_form(X: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Closed-form solution for simple linear regression (one feature).
    """

    if len(X) != len(y):
        raise ValueError("X and y must have the same length")

    if len(X) < 2:
        raise ValueError("At least two data points are required")

    # Implementation will follow
    raise NotImplementedError


def predict(X: List[float], coef: float, intercept: float) -> List[float]:
    """
    Generate predictions for simple linear regression.
    """

    if not X:
        raise ValueError("X must not be empty")

    # Implementation will follow
    raise NotImplementedError
