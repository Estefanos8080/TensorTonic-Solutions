def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    # Write code here
    # pass

    if len(tokens) < 1:
        return tokens
    lis = []
    start = 0
    step = chunk_size - overlap

    while start <= len(tokens):
        chunk = tokens[start : start + chunk_size]
        lis.append(chunk)

        if start + chunk_size >= len(tokens):
            break
            
        start += step

    return lis
        