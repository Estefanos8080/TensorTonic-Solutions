import numpy as np

def zscore_standardize(
    X: list,
    axis: int = 0,
    eps: float = 1e-12
) -> np.ndarray:

    X = np.asarray(X, dtype=float)
    original_shape = X.shape

    # Treat 1D input as one column
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    # For axis=1, transpose so each original row becomes a column
    if axis == 1:
        X = X.T

    number_of_rows, number_of_columns = X.shape
    z_scores = np.zeros_like(X, dtype=float)

    for j in range(number_of_columns):

        # Calculate the mean
        total = 0

        for i in range(number_of_rows):
            total += X[i, j]

        mean_value = total / number_of_rows

        # Calculate population standard deviation
        squared_total = 0

        for i in range(number_of_rows):
            squared_total += (X[i, j] - mean_value) ** 2

        std_value = (squared_total / number_of_rows) ** 0.5

        # Leave this column as zeros when std_value <= eps
        if std_value <= eps:
            continue

        # Calculate z-scores
        for i in range(number_of_rows):
            z_scores[i, j] = (X[i, j] - mean_value) / std_value

    if axis == 1:
        z_scores = z_scores.T

    return z_scores.reshape(original_shape)