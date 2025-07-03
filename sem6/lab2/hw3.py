from main import newton, fixed_point_iteration

def f(x: float) -> float:
    return x**3 + 3.0 * x**2 + 6.0 * x - 1

def f_prime(x: float) -> float:
    return 3 * x**2 + 6 * x + 6

def f_prime_sec(x: float) -> float:
    return 6 * x + 6

def fi(x):
    return (-x**3 - 3*x**2 + 1) / 6.0

a, b = -0.5, 0.5
#x, points = newton(f, f_prime, f_prime_sec, a, b, eps=1e-15)
#xvalues = points["x"]
#yvalues = points["y"]
#
#m = f_prime(-0.5)
#M = f_prime_sec(0.5)
#print(m)
#print(M)
#
#for i, x in enumerate(xvalues):
#    print(i, x)
#
#delta = (M / 2*m) * (abs(xvalues[5] - xvalues[4])**2)
#print(f"{delta:.25f}")


x, points = fixed_point_iteration(fi, f, f_prime_sec, a, b)
xvalues = points["x"]
for i, x in enumerate(xvalues[:6]):
    print(i, round(x, 5))

m = f_prime(-0.5)
M = f_prime_sec(0.5)
delta = (M / 2*m) * (abs(xvalues[5] - xvalues[4]))**2
print(f"{delta:.9f}")
