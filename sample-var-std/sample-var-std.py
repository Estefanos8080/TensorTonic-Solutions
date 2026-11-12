import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    #pass
    # mean
    total = 0
    for n in x:
        total += n

    get_mean = total / len(x)

    # devaiation
    dev_list = []
    for t in x:
        dev = t - get_mean
        dev_list.append(dev)

    total_dev = 0
    for c in dev_list:
        total_dev += c ** 2

    variance = total_dev / (len(x) - 1)
    standard_deviation = variance ** 0.5

    set_dic = {
        "variance": round(variance, 6),
        "standard_deviation": round(standard_deviation, 6)
    }

    return set_dic

    

    