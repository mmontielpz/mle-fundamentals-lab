import numpy as np
from sklearn.linear_model import LinearRegression as SklearnLinearRegression
from src.linear_regression import LinearRegression as ScratchLinearRegression

# --- Reproducibility ---
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# --- Synthetic linear data ---
n_samples = 200
X = np.random.uniform(0, 10, size=(n_samples, 1))

true_coef = 3.5
true_intercept = 2.0
noise = np.random.normal(0, 1.0, size=n_samples)

y = true_coef * X.squeeze() + true_intercept + noise

# --- Train / validation split ---
split_index = int(0.8 * n_samples)
X_train, X_val = X[:split_index], X[split_index:]
y_train, y_val = y[:split_index], y[split_index:]

# --- Scikit-learn baseline ---
sk_model = SklearnLinearRegression()
sk_model.fit(X_train, y_train)

# --- From-scratch implementation ---
scratch_model = ScratchLinearRegression()
scratch_model.fit(X_train.squeeze(), y_train)

# --- Numerical comparison ---
coef_diff = abs(sk_model.coef_[0] - scratch_model.coef_)
intercept_diff = abs(sk_model.intercept_ - scratch_model.intercept_)

print("True coefficient / intercept:")
print(true_coef, true_intercept)

print("\nSklearn coefficient / intercept:")
print(sk_model.coef_[0], sk_model.intercept_)

print("\nScratch coefficient / intercept:")
print(scratch_model.coef_, scratch_model.intercept_)

print("\nAbsolute differences:")
print("Coefficient diff:", coef_diff)
print("Intercept diff:", intercept_diff)

assert coef_diff < 1e-6
assert intercept_diff < 1e-6
