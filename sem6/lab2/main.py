import math
#import matplotlib.pyplot as plt
#import numpy as np
from typing import Callable


def bisection(f: Callable, a: float, b: float, eps=1e-10) -> [float, dict[str|list[float]]]:
    left, right = a, b
    points = {'x': [], 'y': []}
    
    while right > left:
        middle = (right + left) / 2

        points['x'].append(middle)
        points['y'].append(f(middle))

        # возвращаем аргумент, если значение функции достаточно близко к нулю,
        # чтобы избежать бесконечных циклов
        if abs(f(middle)) < eps:
            return middle, points

        if f(left) * f(middle) < 0:
            right = middle
        else:
            left = middle

def secant(f: Callable, a: float, b: float, eps=1e-10) -> [float, dict[str|list[float]]]:
    x, x_prev = b, a

    points = {'x': [], 'y': []}
	
    while abs(x - x_prev) >= eps:
        points['x'].append(x)
        points['y'].append(f(x))
        x, x_prev = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x
        
    return x, points

def fixed_point_iteration(fi: Callable, f: Callable, f_derivative_second: Callable,
                          a: float, b: float, eps=1e-10) -> [float, dict[str|list[float]]]:
    x_0 = b if f(b) ** f_derivative_second(b) > 0 else a
    points = {'x': [], 'y': []}
    while True:
        points['x'].append(x_0)
        points['y'].append(f(x_0))

        x = fi(x_0)
        if abs(x - x_0) < eps:
            break

        x_0 = x

    return x, points

def newton(f: Callable, f_derivative: Callable, f_derivative_second: Callable,
           a: float, b: float, eps=1e-10) -> [float, dict[str|list[float]]]:
    x_0 = b if f(b) * f_derivative_second(b) > 0 else a
    points = {'x': [], 'y': []}

    MAX_ITRS = 100
    num_itrs = 0

    while True:
        points['x'].append(x_0)
        points['y'].append(f(x_0))

        if num_itrs >= MAX_ITRS:
            break

        x = x_0 - f(x_0) / f_derivative(x_0)
        if abs(x - x_0) < eps:
            break

        x_0 = x
        num_itrs += 1

    return x, points

def f(x):
    return x**3 - x

def f_prime(x):
    return 3 * x**2 - 1

def f_prime_sec(x):
    return 6 * x


#a = -1.0/math.sqrt(5)
#b = 1.0/math.sqrt(5)
#x, points = newton(f, f_prime, f_prime_sec, a, b)
#print(points["x"][:2], points["y"][:2])
#xvalues = [points['x'][0], points['x'][0]]
#yvalues = [0, points['y'][0]]
#
#plt.plot([x / 10.0 for x in range(-5, 7)],
#         [f(x / 10.0) for x in range(-5, 7)],
#         'b-', label=r"x^3 - x")
#
#plt.plot(points['x'][0], 0, 'ro')
#plt.annotate(r"$x_0$", xy=(points['x'][0], 0), xytext=(points['x'][0], 0+0.01))
#plt.plot(points['x'][0], points["y"][0], 'ro')
#plt.annotate(r"$f(x_0)$", xy=(points['x'][0], points["y"][0]),
#             xytext=(points['x'][0], points["y"][0]+0.01))
#
#plt.plot(points['x'][1], 0, 'ro')
#plt.annotate(r"$x_1$", xy=(points['x'][1], 0), xytext=(points['x'][1], 0+0.01))
#plt.plot(points['x'][1], points["y"][1], 'ro')
#plt.annotate(r"$f(x_1)$", xy=(points['x'][0], points["y"][1]),
#             xytext=(points['x'][1], points["y"][1]+0.01))
#
#plt.plot(xvalues, yvalues, '--^')
#plt.plot([points["x"][0], points["x"][1]], [points["y"][0], 0], '-->')
#plt.plot([points["x"][1], points["x"][1]], [0, points["y"][1]], '--v')
#plt.plot([points["x"][1], points["x"][0]], [points["y"][1], 0], '--<')
#
#plt.xticks(np.arange(-0.5, 0.6, step=0.1))
#plt.grid(True)
#plt.show()
