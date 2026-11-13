def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    # Write code here
    # pass

    multip_li = []
    # trace_mult = 1

    for n in X:
        new_row = n.copy()
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                new_row.append(n[i] * n[j])
                
        multip_li.append(new_row)

    return multip_li