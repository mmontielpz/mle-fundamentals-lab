import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error

# --- Reproducibility ---
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# --- Data generation ---
n_samples = 200
X = np.linspace(0, 10, n_samples).reshape(-1, 1)
noise = np.random.normal(0.0, 1.0, size=n_samples)

y = (
    0.5 * X.squeeze() ** 2
    + 1.0 * X.squeeze()
    + 5.0
    + noise
)

# --- Train / validation split ---
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=RANDOM_STATE
)

# --- High-complexity feature expansion ---
degree = 10
poly = PolynomialFeatures(degree=degree, include_bias=False)

X_train_poly = poly.fit_transform(X_train)
X_val_poly = poly.transform(X_val)

# --- Feature scaling (numerical stability) ---
scaler = StandardScaler()
X_train_poly = scaler.fit_transform(X_train_poly)
X_val_poly = scaler.transform(X_val_poly)

# --- Models ---
models = {
    "unregularized": LinearRegression(),
    "ridge_regularized": Ridge(alpha=1.0),
}

# --- Evaluation ---
for name, model in models.items():
    model.fit(X_train_poly, y_train)

    y_train_pred = model.predict(X_train_poly)
    y_val_pred = model.predict(X_val_poly)

    train_mse = mean_squared_error(y_train, y_train_pred)
    val_mse = mean_squared_error(y_val, y_val_pred)

    print(f"\nModel: {name}")
    print(f"  Train MSE: {train_mse:.4f}")
    print(f"  Val   MSE: {val_mse:.4f}")
