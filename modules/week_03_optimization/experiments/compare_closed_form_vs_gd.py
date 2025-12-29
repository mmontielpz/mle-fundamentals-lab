import numpy as np

from week_03_optimization.src.gradient_descent import (
    gradient_descent,
)


def closed_form_solution(X, y):
    X_design = np.c_[X, np.ones(len(X))]
    theta = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y
    return theta[0], theta[1]


def main():
    np.random.seed(42)

    X = np.linspace(0, 10, 50)
    y = 3.0 * X + 5.0 + np.random.normal(0, 2, size=len(X))

    w_cf, b_cf = closed_form_solution(X, y)

    w_gd, b_gd, _, iters = gradient_descent(
        X,
        y,
        learning_rate=1e-2,
        max_iterations=500,
        grad_tol=1e-3,
    )

    print("Closed-form solution:")
    print(f"w = {w_cf:.4f}, b = {b_cf:.4f}")

    print("\nGradient Descent solution:")
    print(f"w = {w_gd:.4f}, b = {b_gd:.4f}")
    print(f"Iterations: {iters}")


if __name__ == "__main__":
    main()
