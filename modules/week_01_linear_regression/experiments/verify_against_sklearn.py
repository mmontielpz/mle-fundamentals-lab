import numpy as np
from sklearn.linear_model import LinearRegression as SklearnLinearRegression
from src.linear_regression import LinearRegression

# --- Reproducibility ---
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# -- Synthetic data generation ---
n_samples = 200
X = np.random.rand(n_samples) * 10

true_coef = 3.5
true_intercept = 2.0
noise = np.random.normal(0, 1.0, size=n_samples)

y = true_coef * X + true_intercept + noise

# --- Deterministic shuffle ---
indices = np.random.permutation(n_samples)
X = X[indices]
y = y[indices]

# --- Train / validation split ---
split_index = int(0.8 * n_samples)
X_train, X_val = X[:split_index], X[split_index:]
y_train, y_val = y[:split_index], y[split_index:]

# --- Scikit-learn baseline ---
sk_model = SklearnLinearRegression()
sk_model.fit(X_train.reshape(-1, 1), y_train.tolist())

# --- From-scratch implementation ---
scratch_model = LinearRegression()
scratch_model.fit(X_train.tolist(), y_train.tolist())

# --- Comparison ---
print("True coefficient / intercept:")
print(true_coef, true_intercept)

print("\nSklearn coefficient / intercept:")
print(sk_model.coef_[0], sk_model.intercept_)

print("\nScratch coefficient / intercept:")
print(scratch_model.coef_, scratch_model.intercept_)
