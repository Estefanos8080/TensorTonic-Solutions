import torch

def subsample_keep_probs(
    counts: torch.Tensor, t: float = 1e-5
) -> torch.Tensor:
    counts = counts.to(dtype=torch.float64)
    total = counts.sum().item()

    keep_probs = []
    for count in counts.tolist():
        if count == 0:
            keep_probs.append(1.0)
            continue

        freq = count / total
        keep_probs.append(min(1.0, (t / freq) ** 0.5))

    return counts.new_tensor(keep_probs)