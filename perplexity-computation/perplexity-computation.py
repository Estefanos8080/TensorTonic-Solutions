import math

def perplexity(prob_distributions: list, actual_tokens: list) -> float:
    """
    Returns the sequence perplexity.
    """
    lis_log = []
    for n in range(len(actual_tokens)):
        token_pos = actual_tokens[n]
        tem_pos = prob_distributions[n][token_pos]

        log_n = math.log(tem_pos)
        lis_log.append(log_n)

    total_log = 0
    for t in lis_log:
        total_log += t

    average_prob = -total_log / len(lis_log)

    result = math.exp(average_prob)

    return round(result, 4)
