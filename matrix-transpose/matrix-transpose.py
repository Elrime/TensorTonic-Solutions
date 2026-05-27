import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)

    n, m = A.shape
    B = np.empty((m, n), dtype=A.dtype)

    for i in range(n):
        for j in range(m):
            B[j, i] = A[i, j]

    return B
   
