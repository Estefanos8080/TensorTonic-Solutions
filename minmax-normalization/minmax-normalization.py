
import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    D2_list = []

    if axis == 0:
        for j in range(len(X[0])):
            col = []
            for i in range(len(X)):
                col.append(X[i][j])

            min_num = min(col)
            max_num = max(col)
            range_num = max_num - min_num

            scaled_col = []
            for value in col:
                scaled_col.append(
                    (value - min_num) / max(range_num, eps)
                )

            D2_list.append(scaled_col)

        return np.array(D2_list, dtype=float).T

    elif axis == 1:
        for row in X:
            min_num = min(row)
            max_num = max(row)
            range_num = max_num - min_num

            scaled_row = []
            for value in row:
                scaled_row.append(
                    (value - min_num) / max(range_num, eps)
                )

            D2_list.append(scaled_row)

        return np.array(D2_list, dtype=float)