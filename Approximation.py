import numpy as np


def f_1(t, x):
    return 1 / np.pi * (np.cos(t - x * np.sin(t)))


# Parameters

a = 0
b = np.pi

# Segment splitting

n = 100
d = (b - a) / n


def trapz(f, x):
    xi = a
    xi_1 = xi + d
    s1 = (f(xi_1, x) + f(xi, x)) * d
    for i in range(0, n - 1):
        xi = xi_1
        xi_1 = xi + d
        s = s1
        s1 = s + (f(xi_1, x) + f(xi, x)) * d
    print('Trapz result', -s1 / 2)


"""def simpson(x):
    xi = a
    xi_1 = xi + d
    xi_2 = xi_1 + d
    s1 = d / 3 * (f(xi, x) + 4 * f(xi_1, x) + f(xi_2, x))
    for i in range(0, n - 1):
        xi = xi_1
        xi_1 = xi + d
        xi_2 = xi_1 + d
        s = s1
        s1 = s + d / 3 * (f(xi, x) + 4 * f(xi_1, x) + f(xi_2, x))
    print('Simpson result', -s1 / 2)
"""

print('hello world')
