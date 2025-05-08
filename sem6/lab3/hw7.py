import matplotlib.pyplot as plt
import numpy as np

from main import euler, first_euler_modification, second_euler_modification
from math import exp

N = 13

# task 1
def f1(x, y):
    return y - x

def sol1(x):
    return 16 * exp(x) + x + 1

def sol1_step1(x):
    return 32 * exp(x-1) + x + 1

def sol1_med1(x):
    return 24 * exp(x-1/2) + x + 1

def kas_sol1_med1(x):
    return 25 * x + 13

def kas_sol1(x):
    return 17 * x + 17

def kas_mod2(x):
    return 33 * x + 1

def mod2_line(x):
    return 21.82 * x + 12.18

H1 = 1.0
N1 = 2

x1_0 = 0.0
y1_0 = float(N + 4)
x1_euler, y1_euler, point_euler1 = euler(f1, N1, H1, x1_0, y1_0)

x1_0 = 0.0
y1_0 = float(N + 4)
x1_first_mod, y1_first_mod, point_first_mod = first_euler_modification(f1, N1, H1, x1_0, y1_0)

x1_0 = 0.0
y1_0 = float(N + 4)
x1_second_mod, y1_second_mod, point_second_mod = second_euler_modification(f1, N1, H1, x1_0, y1_0)

print(point_euler1)
print(point_first_mod)
print(point_second_mod)

plt.subplot(221)
plt.title("Метод Эйлера")
plt.plot([x / 10 for x in range(21)], [sol1(x/10) for x in range(21)],
         color="blue", label="1. точное решение ЗК")
plt.annotate("1", (2.0, sol1(2.0)), (2.0 + 0.01, sol1(2.0)))

plt.plot("x", "y", "-m.", data=point_euler1, label="2. численное решение")
plt.annotate("2", (point_euler1["x"][2], point_euler1["y"][2]),
             (point_euler1["x"][2] + 0.01, point_euler1["y"][2]))

plt.plot([x / 10 for x in range(21)], [sol1_step1(x/10) for x in range(21)],
         color="black", label=r"3. Интегральная кривая проходящяя через $x_1$")
plt.annotate("3", (2.0, sol1_step1(2.0)), (2.0 + 0.01, sol1_step1(2.0)))

plt.grid(True)
plt.xticks(np.arange(0, 2.1, step=0.1))
plt.legend(loc="upper left")

med_point1_x = 0.5
med_point1_y = 25.5

plt.subplot(222)
plt.title("Первая модификация")
plt.plot([x / 10 for x in range(11)], [sol1(x/10) for x in range(11)],
         color="blue", label="1. точное решение ЗК")
plt.annotate("1", (1.0, sol1(1.0)), (1.0 + 0.01, sol1(1.0)))

plt.plot(point_first_mod["x"][:2], point_first_mod["y"][:2], "-m.",
         label="2. численное решение")
plt.annotate("2", (point_first_mod["x"][1], point_first_mod["y"][1]),
             (point_first_mod["x"][1] + 0.01, point_first_mod["y"][1]))

plt.plot([x / 10 for x in range(11)], [sol1_med1(x/10) for x in range(11)],
         color="black", label=r"3. Интегральная кривая проходящяя через $x_{1/2}$")
plt.annotate("3", (1.0, sol1_med1(1.0)), (1.0+0.05, sol1_med1(1.0)))

plt.plot([point_first_mod["x"][0], med_point1_x],
         [point_first_mod["y"][0], med_point1_y], label="4. касательная к решению")
plt.annotate("4", (med_point1_x, med_point1_y), (med_point1_x+0.01, med_point1_y))

plt.plot([med_point1_x, 1.0], [med_point1_y, kas_sol1_med1(1.0)],
         label=r"5. касательная к кривой, проходящей через $x_{1/2}$")
plt.annotate("5", (1.0, kas_sol1_med1(1.0)),
        (1.0+0.01, kas_sol1_med1(1.0)))
plt.grid(True)
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.legend(loc="upper left")

plt.subplot(223)
plt.title("Вторая модификация")
plt.plot([x / 10 for x in range(16)], [sol1(x/10) for x in range(16)],
         color="blue", label="1. точное решение ЗК")
plt.annotate("1", (1.5, sol1(1.5)),
             (1.5+0.01, sol1(1.5)))

plt.plot([x / 10 for x in range(16)], [sol1_step1(x/10) for x in range(16)],
         color="black", label=r"2. Интегральная кривая проходящяя через $x_1$")
plt.annotate("2", (1.5, sol1_step1(1.5)), (1.5 + 0.01, sol1_step1(1.5)))

plt.plot(point_second_mod["x"][:2], point_second_mod["y"][:2], "-m.",
         label="3. численное решение")
plt.annotate("3", (point_second_mod["x"][1], point_second_mod["y"][1]),
             (point_second_mod["x"][1] + 0.01, point_second_mod["y"][1]))

plt.plot([point_second_mod["x"][0], 1.5],
         [point_second_mod["y"][0], kas_sol1(1.5)], label="4. касательная к решению")
plt.annotate("4", (1.5, kas_sol1(1.5)),
             (1.5+0.01, kas_sol1(1.5)))

plt.plot([point_euler1["x"][1], 1.5],
         [point_euler1["y"][1], kas_mod2(1.5)],
         label="5. касательная к приближению методом эйлера")
plt.annotate("5", (1.5, kas_mod2(1.5)),
             (1.5+0.01, kas_mod2(1.5)))

plt.plot([0, 1], [mod2_line(0.0), mod2_line(1.0)],
         label="6. прямая со средним углом наклона")
plt.annotate("6", (1.0, mod2_line(1.0)),
             (1.0+0.01, mod2_line(1.0)))
plt.grid(True)
plt.xticks(np.arange(0, 1.6, step=0.1))
plt.legend(loc="upper left")

plt.show()
