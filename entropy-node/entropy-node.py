import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    # pass
    if len(y) == 0:
        return 0.0

    counts = {}

    for label in y:
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    
    store_log = []

    for label in counts:
        p = counts[label] / len(y)
        n = -p * np.log2(p)
        store_log.append(n)
    
    return_float = 0.0

    for num in store_log:
        return_float += num

    return float(return_float)
        

    