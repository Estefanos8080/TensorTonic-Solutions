def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    # Write code here
    # pass
    counts = {}

    for value in values:
        counts[value] = counts.get(value, 0) + 1

    lis_freq = []

    for value in values:
        lis_freq.append(counts[value] / len(values))

    return lis_freq
    