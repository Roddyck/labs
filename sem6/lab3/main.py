import matplotlib.pyplot as plt

from typing import Callable
from math import exp

def euler(f: Callable[[float, float], float], n: int, h: float, x: float, y: float) -> (float, float, dict[str|list[float]]):
    points = {"x": [x], "y": [y]}

    for i in range(n):
        y += h * f(x,y)
        x += h

        points["x"].append(x)
        points["y"].append(y)

    return x, y, points

def first_euler_modification(f: Callable[[float, float], float], n: int, h: float,
                             x: float, y: float) -> (float, float, dict[str|list[float]]):
    points = {"x": [x], "y": [y]}

    for i in range(n):
        x_medium = x + h / 2.0
        y_medium = y + h / 2.0 * f(x,y)
        y += h * f(x_medium, y_medium)
        x += h

        points["x"].append(x)
        points["y"].append(y)

    return x, y, points

def second_euler_modification(f: Callable[[float, float], float], n: int, h: float,
                             x: float, y: float) -> (float, float, dict[str|list[float]]):
    points = {"x": [x], "y": [y]}

    for i in range(n):
        y_pred = y + h * f(x, y)
        y += h * ((f(x, y) + f(x + h, y_pred)) / 2.0)
        x += h

        points["x"].append(x)
        points["y"].append(y)

    return x, y, points

def runge_kutta(f: Callable[[float, float], float], n: int, h: float, alpha: float,
                x: float, y: float):
    for i in range(n):
        x_pred = x + alpha * h
        y_pred = y + alpha * h * f(x,y)
        y += h * ((1 - 1/2*alpha) * f(x, y) + (1/2*alpha) * f(x_pred, y_pred))
        x += h

    return x, y

def frange(end: float, start=0.0, step=0.1):
    while start < end:
        yield start
        start += step
