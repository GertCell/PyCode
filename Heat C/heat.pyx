import cython
import numpy as np


def TwoDimLaser():

    # entering constants

    cdef int Nx = 150, Ny = 150, Nt = 100, i, j, t
    cdef double Ly = 0.05, Lx = 0.005, t_end = 5.0
    cdef double l = 18.0, po = 4500.0, c = 530.0, T0 = 200.0, Th = 1500.0, Tc = 200.0

    # summation steps

    cdef double a = l / (po * c)
    cdef double hx = Lx / (Nx - 1)
    cdef double hy = Ly / (Ny - 1)
    cdef double tau = t_end / Nt

    # temp arrays

    T = np.zeros((Nx, Ny))
    alfa = np.zeros(Ny)
    beta = np.zeros(Ny)
    t = -1
    for i in range(0, Nx):
        for j in range(0, Ny):
            T[i, j] = T0
    for time in np.linspace(0, t_end, Nx - 5):
        t += 1

        for j in range(0, Ny):

            alfa[0] = 0
            beta[0] = Tc

            for i in range(1, Nx - 1):
                ai = l / hx ** 2
                bi = 2 * l / hx ** 2 + po * c / tau
                fi = -po * c * T[i, j] / tau

                alfa[i] = ai / (bi - ai * alfa[i - 1])
                beta[i] = (ai * beta[i - 1] - fi) / (bi - ai * alfa[i - 1])

            for i in range(Nx - 2, -1, -1):
                T[i, j] = alfa[i] * T[i + 1, j] + beta[i]

        for i in range(1, Nx - 1):

            alfa[0] = 2.0 * a * tau / (2 * a * tau + hy ** 2)
            beta[0] = hy ** 2 * T[i, 1] / (2 * a * tau + hy ** 2)

            for j in range(1, Ny - 1):
                ai = l / hy ** 2
                bi = 2 * l / hy ** 2 + po * c / tau
                fi = -po * c * T[i, j] / tau

                alfa[j] = ai / (bi - ai * alfa[j - 1])
                beta[j] = (ai * beta[j - 1] - fi) / (bi - ai * alfa[j - 1])

            T[i, Ny - 1] = (2.0 * a * tau * beta[Ny - 2] + hy ** 2 * T[i, Ny - 1]) / (
                        2.0 * a * tau * (1.0 - alfa[Ny - 2]) + hy ** 2)

            for j in range(Ny - 2, -1, -1):
                T[i, j] = alfa[j] * T[i, j + 1] + beta[j]
            #             if int(t/3) - t/3 == 0:
            T[Nx - 1, t] = Th

            if time > t_end / 2.0: break
    np.delete(T, (Nx - 1), axis=0)
    print(Nx, Ny)
    return T







