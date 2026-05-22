import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.array(k)
    E = 1 / p
    P = (1 - p)** (k - 1) * p
    return (P, E)