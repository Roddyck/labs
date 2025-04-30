from typing import Callable
from math import sin, cos

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

    while True:
        points['x'].append(x_0)
        points['y'].append(f(x_0))

        x = x_0 - f(x_0) / f_derivative(x_0)
        if abs(x - x_0) < eps:
            break

        x_0 = x

    return x, points