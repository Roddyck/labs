from main import euler, first_euler_modification, second_euler_modification
from math import exp, fabs, sin

N = 13

# task 1
def f1(x, y):
    return y - x

def sol1(x):
    return 16 * exp(x) + x + 1

x1_0 = 0.0
y1_0 = float(N + 4)
h1 = 0.1
n1 = 1
TRUE_VALUE1 = sol1(0.1)

x1_euler, y1_euler, point_euler1 = euler(f1, n1, h1, x1_0, y1_0)
print("True value:", TRUE_VALUE1)
print("Euler method:", y1_euler)
print("Euler abs error:", round(fabs(y1_euler - TRUE_VALUE1), 4))

x1_0 = 0.0
y1_0 = float(N + 4)
x1_first_mod, y1_first_mod, point_first_mod = first_euler_modification(f1, n1, h1, x1_0, y1_0)
print("\nTrue value:", TRUE_VALUE1)
print("First modification method:", y1_first_mod)
print("First modification abs error:", round(fabs(y1_first_mod - TRUE_VALUE1), 4))

x1_0 = 0.0
y1_0 = float(N + 4)
x1_second_mod, y1_second_mod, point_second_mod = second_euler_modification(f1, n1, h1, x1_0, y1_0)
print("\nTrue value:", TRUE_VALUE1)
print("Second modification method:", y1_second_mod)
print("Second modification abs error:", round(fabs(y1_second_mod - TRUE_VALUE1), 4))

# task 2
GAMMA = 2 * 17/21
h2 = 0.1
y2_0 = 13/4
x2_0 = 0.2
n2 = 1

def f2(x, y):
    return 0.133 * (x**2 + sin(GAMMA * x)) + 0.872 * y

print("\nPART 2:\n")
x2_euler, y2_euler, point_euler2 = euler(f2, n2, h2, x2_0, y2_0)
print("Euler method:", round(y2_euler, 5))

y2_0 = 13/4
x2_0 = 0.2
x2_first_mod, y2_first_mod, point_first_mod = first_euler_modification(f2, n2, h2, x2_0, y2_0)
print("First modification method:", round(y2_first_mod, 5))

y2_0 = 13/4
x2_0 = 0.2
x2_second_mod, y2_second_mod, point_second_mod = second_euler_modification(f2, n2, h2, x2_0, y2_0)
print("Second modification method:", round(y2_second_mod, 5))
