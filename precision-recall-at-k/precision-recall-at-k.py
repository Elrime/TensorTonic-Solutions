def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = recommended[:k]

    Precision_K = len(set(top_k) & set(relevant)) / k
    Recall_K = len(set(top_k) & set(relevant)) / len(relevant)

    return [Precision_K, Recall_K]
   