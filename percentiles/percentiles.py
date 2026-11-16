
import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Sort values first
    x = sorted(x)

    list_prect = []

    for pre in q:
        position = (pre / 100) * (len(x) - 1)
        lower = int(position)
        upper = min(lower + 1, len(x) - 1)

        weight = position - lower

        result = x[lower] + weight * (x[upper] - x[lower])

        list_prect.append(result)

    return np.array(list_prect, dtype=float)
