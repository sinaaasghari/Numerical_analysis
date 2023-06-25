import numpy as np

def romberg_integration(f, a, b, n):

    r = np.zeros((n, n), float)
    h = b - a

    r[0, 0] = 0.5 * h * (f(a) + f(b))
    for i in range(1, n):
        h *= 0.5
        summ = 0.0
        for k in range(1, 2**i, 2):
            summ += f(a + k * h)
        r[i, 0] = 0.5 * r[i-1, 0] + summ * h

        for j in range(1, i+1):
            r[i, j] = r[i, j-1] + (r[i, j-1] - r[i-1, j-1]) / (4**j - 1)

    return r[n-1, n-1]


def f(x):
    return  x**2 + x

a = 0.0
b = 1.0
n = 5

result = romberg_integration(f, a, b, n)
print("Approximate integral:", result)
