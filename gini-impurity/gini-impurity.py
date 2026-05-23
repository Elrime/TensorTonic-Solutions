import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    y_left = np.array(y_left)
    y_right = np.array(y_right)
    def gini(y):
      if len(y) == 0:
        return 0.0
      else:
        _, counts = np.unique(y, return_counts=True)
        probs = counts / len(y)
        return (1 - np.sum(probs ** 2))[()]

    N = len(y_left) + len(y_right)

    if N == 0:
      return 0.0

    Gini_split = (len(y_left) / N * gini(y_left) + len(y_right) / N * gini(y_right))[()]

    return Gini_split
    
    
    