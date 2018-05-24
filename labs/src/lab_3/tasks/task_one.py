import numpy as np
import math as m
from matplotlib import pyplot as pl


def f(x):
    return m.exp(3 * x) / ((x ** 3) + m.sqrt(x + 1))


def ddf(x):
    return (9 * m.exp(3 * x)) / (x ** 3 + m.sqrt(x + 1)) - (
            6 * m.exp(3 * x) * (3 * x ** 2 + 1 / (2 * m.sqrt(x + 1)))) / (x ** 3 + m.sqrt(x + 1)) ** 2 + m.exp(
        3 * x) * ((2 * (3 * x ** 2 + 1 / (2 * m.sqrt(x + 1))) ** 2) / (x ** 3 + m.sqrt(x + 1)) ** 3 - (
            6 * x - 1 / (4 * (x + 1) ** (3 / 2))) / (x ** 3 + m.sqrt(x + 1)) ** 2)


def source_function_plot(a, b, n):
    pl.figure("Source function")

    x = np.linspace(a, b, n)
    y = []
    step = (b - a) / n

    for i in range(n):
        y.append(f(a + i * step))

    pl.plot(x, y, 'purple', label='source function')
    pl.legend()
    pl.grid()
    pl.show()


def ddf_plot(a, b):
    pl.figure("ddf")
    i = np.linspace(a, b, 100)

    m2 = []
    for j in range(100):
        m2.append(ddf(i[j]))

    pl.plot(i, m2, 'red', label='ddf')
    pl.legend()
    pl.grid()
    pl.show()


# def trapezoidal_integration(a, b, n):
#     h = (b - a) / n
#     res = 0.5 * (f(a) + f(b))
#     for i in range(1, n):
#         res += f(a + i * h)
#     return h * res
#
#
# def trapezoidal_integration_with_precision(a, b, eps):
#     n = 0
#     prev_res = float('inf')
#     res = 0
#     while abs(prev_res - res) > eps:
#         n += 1
#         prev_res = res
#         res = trapezoidal_integration(a, b, n)
#     return res


def trapezoidal_integration(a, b, eps):
    h = m.sqrt(12 * eps / (ddf(b) * (b - a)))
    n = int((b - a) / h)
    res = 0.5 * (f(a) + f(b))
    for i in range(1, n + 1):
        res += f(a + i * h)
    return h * res


def simpson_integration(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(2, n - 1, 2):
        res += 2 * f(a + i * h)
    for i in range(1, n, 2):
        res += 4 * f(a + i * h)
    return h * res / 3


def run():
    a = 2
    b = 3
    eps = 10 ** -5
    simpson_n = 10

    source_function_plot(a, b, simpson_n)
    ddf_plot(a, b)

    print('Trapezoidal result:', trapezoidal_integration(a, b, eps), 'for eps =', eps)
    print('Simpson result:', simpson_integration(a, b, simpson_n), 'for n =', simpson_n)


if __name__ == '__main__':
    run()
