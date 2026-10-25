import math

def binomialPMF(n: int, p: float, k: int) -> float:
    return math.comb(n, k) * math.pow(p, k) * math.pow(1.0 - p, n-k)

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    cdf = 0.0
    for i in range(k+1):
        cdf += binomialPMF(n, p, i)
    return {
        "pmf": binomialPMF(n, p, k),
        "cdf": float(cdf)
    }