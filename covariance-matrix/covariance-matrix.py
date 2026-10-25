import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    centered = X - np.mean(X, axis=0)
    return (centered.T @ centered) / (len(X)-1)