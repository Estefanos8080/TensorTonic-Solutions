import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    # pass
    put_M_lis = []
    for n in range(0, len(x)):
        if len(p) > 0:
            y = x[n] * p[n]
            put_M_lis.append(y)

    final_add = 0
    for t in put_M_lis:
        final_add += t

    return float(final_add)
        