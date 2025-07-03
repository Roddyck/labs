from main import newton, fixed_point_iteration

def f(x: float) -> float:
    return x**3 + 0.4 * x**2 + 0.6 * x - 1.6

def f_prime(x: float) -> float:
    return 3 * x**2 + 0.8 * x + 0.6

def f_prime_sec(x: float) -> float:
    return 6 * x + 0.8

a, b = 0.0, 1.0
x, points = newton(f, f_prime, f_prime_sec, a, b)
xvalues = points["x"]
yvalues = points["y"]

m = f_prime(0.0)
M = f_prime_sec(1.0)
print(m)
print(M)

for i, x in enumerate(xvalues[:3]):
    print(i, x)

print(xvalues[2] - xvalues[1])
delta = (M / 2*m) * ((abs(xvalues[2] - xvalues[1]))**2)
print(f"{delta:.25f}")
