from sage.all import RealField, exp, sqrt, pi

def half_gaussian_normalizing_constant(sigma_value, bits):
    """
    Compute the normalizing constant C for the discrete half-Gaussian pmf on z >= 0:
    """
    R = RealField(bits)
    sigma = R(sigma_value)

    q = exp(-R(1)/(2* (sigma ** 2)))

    # theta_3(0; q) = 1 + 2 sum_{n=1}^∞ q^(n^2).
    # We'll sum until the next term is below 2^(-bits).
    t3 = R(1)
    n = 1
    while True:
        term = 2 * (q ** (n * n))
        if term < 2**(-bits):
            break
        t3 += term
        n += 1

    # sum_{z=0}^∞ exp(-z^2/(2*sigma^2)) = (theta_3(0; q) + 1)/2
    normalizing_constant = (t3 + 1) / 2
    return normalizing_constant

C = half_gaussian_normalizing_constant(sigma_value=1.8205, bits=400)
print("Normalizing constant =", C)
