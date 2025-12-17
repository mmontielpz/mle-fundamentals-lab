import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from src.linear_regression import fit_closed_form, predict

# --- Reproducitiblity --
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# --- Synthetic data generation
# y = beta * x + intercept + noise
n_samples = 200
X = np.random.rand(n_samples) * 10

true_coef = 3.5
true_intercept = 2.0
noise = np.random.normal(0, 1.0, size=n_samples)

y = true_coef * X + true_intercept + noise

# --- Train / validation split (deterministic) ---
split_index = int(0.8 * n_samples)
X_train, X_val = X[:split_index], X[split_index:]
y_train, y_val = y[:split_index], y[split_index:]

# --- Scikit-learn baseline ---
sk_model = LinearRegression()
sk_model.fit(X_train.reshape(-1, 1), y_train)
y_sk_pred = sk_model.predict(X_val.reshape(-1, 1))

# --- From-scracth implementation ---
coef, intercept = fit_closed_form(
    X_train.tolist(),
    y_train.tolist()
)

y_scratch_pred = predict(
    X_val.tolist(),
    coef,
    intercept
)

# --- Comparison ---
mse_sklearn = mean_squared_error(y_val, y_sk_pred)
mse_scratch = mean_squared_error(y_val, y_scratch_pred)

print("Sklearn coefficient / intercept:")
print(sk_model.coef_[0], sk_model.intercept_)

print("\nScratch coefficient / intercept:")
print(coef, intercept)

print("\nValidation MSE:")
print("Sklearn:", mse_sklearn)
print("Scratch:", mse_scratch)
