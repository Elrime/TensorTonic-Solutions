import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array(x)
    PMF = np.where(x == 1, p, 1-p)
    q_2 = p * (1-p)

    return (PMF, p, q_2)
  