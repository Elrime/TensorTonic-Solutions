import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    value, counts = np.unique(y, return_counts=True)
    probabilities = counts / counts.sum()

    non_zero_prob = probabilities[probabilities > 0]

    entropy = -np.sum(non_zero_prob * np.log2(non_zero_prob))

    return entropy