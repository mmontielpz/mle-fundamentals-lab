import numpy as np


def mse_loss(w, b, X, y):
    y_pred = w * X + b
    return np.mean((y - y_pred) ** 2)


def mse_gradients(w, b, X, y):
    y_pred = w * X + b
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    return dw, db


def gradient_descent(
    X,
    y,
    learning_rate,
    max_iterations,
    grad_tol=None,
    loss_tol=None,
):
    w, b = 0.0, 0.0
    loss_history = []

    prev_loss = None

    for i in range(max_iterations):
        dw, db = mse_gradients(w, b, X, y)

        w -= learning_rate * dw
        b -= learning_rate * db

        loss = mse_loss(w, b, X, y)
        loss_history.append(loss)

        if grad_tol is not None:
            grad_norm = np.sqrt(dw**2 + db**2)
            if grad_norm < grad_tol:
                return w, b, loss_history, i + 1

        if loss_tol is not None and prev_loss is not None:
            if abs(prev_loss - loss) < loss_tol:
                return w, b, loss_history, i + 1

        prev_loss = loss

    return w, b, loss_history, max_iterations
