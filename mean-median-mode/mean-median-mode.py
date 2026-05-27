import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)

    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x.flatten()).most_common(1)[0][0]

    return float(mean), float(median), float(mode)