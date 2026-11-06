## Standardization vs Normalization

**Standardization (Z-score)**:

- Centers at mean 0, scales to std 1
- Unbounded output range
- Based on mean and std (sensitive to outliers)
- Good for: Gaussian-like distributions, many ML algorithms

**Normalization (Min-Max)**:

- Scales to fixed range [0, 1]
- Bounded output range
- Based on min and max (very sensitive to outliers)
- Good for: Neural networks, bounded domains