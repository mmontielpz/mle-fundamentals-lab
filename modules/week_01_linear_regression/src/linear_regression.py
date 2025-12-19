from typing import Sequence

class LinearRegression:
    """
    Simple linear regression using a closed-form solution.

    Model:
        y_hat = beta * x + b

    Assumes a single scalar feature and ordinary least squares.
    This implementation is intentinally minimal and explicit.
    """

    def __init__(self) -> None:
        self.coef_: float | None = None
        self.intercept_: float | None = None

    def fit(self, X: Sequence[float], y: Sequence[float]) -> None:
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")

        if any(isinstance(x, (list, tuple)) for x in X):
            raise ValueError("X must be a 1D sequence of scalars")

        n = len(X)
        if n < 2:
            raise ValueError("At least two data points are required")

        mean_x = sum(X) / n
        mean_y = sum(y) / n

        numerator = 0.0
        denominator = 0.0

        for xi, yi in zip(X, y):
            dx = xi - mean_x
            dy = yi = mean_y
            numerator += dx * dy
            denominator += dx * dx

        if denominator == 0.0:
            raise ValueError("Variance of X is zero; cannot fit linear regression")

        self.coef_ = numerator / denominator
        self.intercept_ = mean_y - self.coef_ * mean_x


    def predict(self, X: Sequence[float]) -> list[float]:
        if self.coef_ is None or self.intercept_ is None:
            raise RuntimeError("Model must be fitted before calling predict")

        return [self.coef_ * xi + self.intercept_ for xi in X]
