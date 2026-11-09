def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    # pass

    list = []
    for n in tokens:
        if n not in stopwords:
            list.append(n)

    return list
            