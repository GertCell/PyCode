import numpy as np


def f(t, x, m):
    return 1 / np.pi * (np.cos(m*t - x * np.sin(t)))


# Parameters

a = 0
b = np.pi

# Segment splitting

n = 100
d = (b - a) / n


def trapz(x, m):
    ti = a
    ti_1 = ti + d
    s1 = (f(ti_1, x, m) + f(ti, x, m)) * d
    for i in range(0, n - 1):
        ti = ti_1
        ti_1 = ti + d
        s = s1
        s1 = s + (f(ti_1, x, m) + f(ti, x, m)) * d
    print('Trapz result', -s1 / 2)
    return -s1/2


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


def bessel_derivative(g):
    dx = 0.1
    for x in range(0, 100):
        g = (trapz(x + dx, 0) - trapz(x - dx, 0)) / 2 / dx
        print(g)
    return g


bessel_derivative(g)
