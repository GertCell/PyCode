
# Program checks the equation for Bessel functions

import numpy as np


def f(t, x, m):  # Bessel function
    return 1 / np.pi * (np.cos(m * t - x * np.sin(t)))


# Parameters (boundaries)

a = 0
b = np.pi

# Segment splitting

n = 8
d = (b - a) / n


def trapz(x, m):  # Trapezoid integration method
    ti = a
    ti_1 = ti + d
    s1 = (f(ti_1, x, m) + f(ti, x, m)) * d
    for i in range(0, n - 1):
        ti = ti_1
        ti_1 = ti + d
        s = s1
        s1 = s + (f(ti_1, x, m) + f(ti, x, m)) * d
    # print('Trapz result', -s1 / 2)
    return -s1/2


def simpson(x, m):  # Simpson's integration method
    ti = a
    ti_1 = ti + d
    ti_2 = ti_1 + d
    s1 = d / 3 * (f(ti, x, m) + 4 * f(ti_1, x, m) + f(ti_2, x, m))
    for i in range(0, n - 1):
        ti = ti_1
        ti_1 = ti + d
        ti_2 = ti_1 + d
        s = s1
        s1 = s + d / 3 * (f(ti, x, m) + 4 * f(ti_1, x, m) + f(ti_2, x, m))
    # print('Simpson result', -s1 / 2)
    return -s1/2


def bessel_trapz():  # Two steps
    dx = 0.1
    g, g1 = 0, 0
    for x in range(0, 100):  # 1st x variable will be given here
        g = (trapz(x + dx, 0) - trapz(x - dx, 0)) / 2 / dx  # after cycle took x, it's needed to solve the integral
        g1 = trapz(x, 1)
    print('sum trapezoid method', g+g1)
    return 0


def bessel_simpson():  # Principle is the same
    dx = 0.1
    g, g1 = 0, 0
    for x in range(0, 100):
        g = (simpson(x + dx, 0) - simpson(x - dx, 0)) / 2 / dx
        g1 = simpson(x, 1)
    print('sum simpson method', g+g1)
    return 0


bessel_trapz()
bessel_simpson()
