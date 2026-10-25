import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    total = 0
    for a, b in zip(x, y):
        total += (a * b)
    return float(total)