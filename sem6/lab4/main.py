import math
def runge_kutta(f, n, h, x_0, y_0): 
    iterations = []

    x = x_0;
    y = y_0;

    for i in range(n):
        l1 = f(x, y);
        l2 = f(x + h/2.0, y + h/2.0 * l1);
        l3 = f(x + h/2.0, y + h/2.0 * l2);
        l4 = f(x + h, y + h * l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y += h * l;
        x += h;

        iterations.append(y);

    return iterations;

def func2(x, y):
    return y - 2.0*x / y;

def solution2(x):
    return math.sqrt(2.0 * x + 288.0 * math.exp(2.0 * x));

n = 5
sol_true = solution2(1.0)
x_0 = 0
y_0 = 17
prev_error = 0.0;
while n <= 80:
    runge_kutta_res = runge_kutta(func2, n, 1.0/n, x_0, y_0);
    res = runge_kutta_res[-1]
    error = abs(res - sol_true);

    print(f"Runge Kutta method value for n = {n}: {res}")
    print(f"Real value: {sol_true}")
    if n > 5:
        print(f"Current error less than previous in {prev_error/error:.6f} times")

    prev_error = error;
    n *= 2;
