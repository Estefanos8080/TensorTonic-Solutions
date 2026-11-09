import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    # Write code here
    # pass
    lis = []

    count = 0

    for n in vocab: 
        count = 0

        for token in tokens:
            if n == token:
                count += 1
        lis.append(count)    
    return np.array(lis, dtype=int)
            

    