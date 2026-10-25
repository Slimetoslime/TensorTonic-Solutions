import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dotProduct = np.dot(a, b)
    aNorm, bNorm = np.linalg.norm(a), np.linalg.norm(b)
    if aNorm == 0 or bNorm == 0: return float(0)
    return float(dotProduct / (aNorm * bNorm))
