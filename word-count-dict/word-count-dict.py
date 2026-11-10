def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    # pass
    set_counter = {}
    if len(sentences) < 1:
            return set_counter

    for group in sentences:
        for word in group:
            if word in set_counter:
                set_counter[word] += 1
            else:
                set_counter[word] = 1

    return set_counter
                    
    