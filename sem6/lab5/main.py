import argparse

import matplotlib.pyplot as plt

from math import e, exp
from typing import Callable
from prettytable import PrettyTable


def diff_scheme1(step: float, y0: float, y1: float, x0: float) -> float:
    return (4 * y1 - y0 * (2 + step) - 2 * step**2) / (2 - step)


def true_sol1(x: float) -> float:
    return 2.0 * exp(x) / (e - 1) + x + (3 * e - 5) / (e - 1)


def diff_scheme2(step: float, y0: float, y1: float, x0: float) -> float:
    return (
        y1 * (2 / step**2 + 2 * x0**2)
        + y0 * (-1 / step**2 + (x0 + 1) / 2 * step)
        - 2 * x0**5
        + 3 * x0**3
        + 6 * x0
        + x0**2
    ) / (1 / step**2 + (x0 + 1) / 2 * step)


def true_sol2(x: float) -> float:
    return x**3 + 1


def diff_equation_solve(
    scheme: Callable[[float, float, float, float], float],
    y0: float,
    y1: float,
    x0: float,
    num_iters: int,
    step: float,
) -> list[float]:

    iterations: list[float] = [y0, y1]
    y_0, y_1, x_0 = y0, y1, x0

    for i in range(num_iters - 1):
        # такое количество для того, чтобы если, например, num_iters = 10, то len(iterations) было равно 10
        # ибо уже есть два начальных приближения

        y_next = scheme(step, y_0, y_1, x_0)
        iterations.append(y_next)

        y_0 = y_1
        y_1 = y_next
        x_0 += step

    return iterations


def problem_solve(
    scheme: Callable[[float, float, float, float], float],
    y0: tuple[float, float],
    y1: tuple[float, float],
    x0: float,
    num_iters: int,
    step: float,
    beta: float,
    true_sol: Callable[[float], float],
) -> tuple[PrettyTable, list[float], list[float], list[float], float]:
    first_problem_itrs = diff_equation_solve(scheme, y0[0], y1[0], x0, num_iters, step)
    second_problem_itrs = diff_equation_solve(scheme, y0[1], y1[1], x0, num_iters, step)
    mu = (beta - second_problem_itrs[-1]) / (
        first_problem_itrs[-1] - second_problem_itrs[-1]
    )

    solution: list[float] = []
    for i in range(num_iters + 1):
        y = mu * first_problem_itrs[i] + (1 - mu) * second_problem_itrs[i]
        solution.append(y)

    x_0: float = x0
    mean_error = 0.0

    table = PrettyTable()
    table.field_names = ["i", "x_0", "y*", "y**", "y", "true value", "abs error"]
    for i, (y_first, y_second, y_sol) in enumerate(
        zip(first_problem_itrs, second_problem_itrs, solution)
    ):
        true_value = true_sol(x_0)
        abs_error = abs(y_sol - true_value)
        mean_error += abs_error

        table.add_row(
            [
                i,
                round(x_0, 5),
                round(y_first, 5),
                round(y_second, 5),
                round(y_sol, 5),
                round(true_value, 5),
                round(abs_error, 10),
            ]
        )
        x_0 += step

    mean_error /= num_iters

    return table, first_problem_itrs, second_problem_itrs, solution, mean_error


def show_plots(
    sol: Callable[[float], float],
    x0: float,
    x1: float,
    itrs1: list[float],
    itrs2: list[float],
    itrs_sol: list[float],
) -> None:

    xs: list[float] = [x / 10.0 for x in range(int(x0 * 10), int(x1 * 10) + 1)]
    true_y: list[float] = [sol(x / 10.0) for x in range(int(x0 * 10), int(x1 * 10) + 1)]

    plt.plot(xs, itrs1, "r-", label=r"$y^{\star}$")
    plt.plot(xs, itrs2, "m-", label=r"$y^{\star\star}$")
    plt.plot(xs, itrs_sol, "bs", label="Приближение")
    plt.plot(xs, true_y, "g-", label="Точное решение")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()


def main():
    def part1():
        h = 0.1
        y0 = (3.0, 3.0)
        y1 = (3.0, h + 3.0)
        x0 = 0.0
        x1 = 1.0
        n = 10
        beta = 6.0

        table, itrs1, itrs2, sol, _ = problem_solve(
            diff_scheme1, y0, y1, x0, n, h, beta, true_sol1
        )
        print(table)
        show_plots(true_sol1, x0, x1, itrs1, itrs2, sol)

    def part2():
        h = 0.1
        y0 = (1.0, 1.0)
        y1 = (1.0, h + 1.0)
        x0 = 0.0
        x1 = 1.0
        n = 10
        beta = 2.0

        table, itrs1, itrs2, sol, _ = problem_solve(
            diff_scheme2, y0, y1, x0, n, h, beta, true_sol2
        )
        print(table)
        show_plots(true_sol2, x0, x1, itrs1, itrs2, sol)

    def part3():
        n = 10
        mean_errors: list[float] = []
        while n <= 80:
            x0 = 0.0
            x1 = 1.0
            h = (x1 - x0) / n
            y0 = (3.0, 3.0)
            y1 = (3.0, h + 3.0)
            beta = 6.0

            table, _, _, _, mean_error = problem_solve(
                diff_scheme1, y0, y1, x0, n, h, beta, true_sol1
            )
            mean_errors.append(mean_error)
            print(f"Table for n = {n}:")
            print(table)
            print(f"mean error = {mean_error:.8f}")

            n *= 2

        error_diff = mean_errors[-2] / mean_errors[-1]
        print(
            f"При увеличении количества шагов в 2 раза погрешность уменьшается примерно в {round(error_diff, 1)} раза"
        )
        print(f"Следовательно порядок сходимости = {round(error_diff / 2, 1)}")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pos_arg",
        type=int,
        help="Обязательное целое число [1-3] - номер части задания для выполнения",
    )
    args = parser.parse_args()

    if args.pos_arg > 3:
        parser.error("pos_arg не может быть больше, чем 3")

    if args.pos_arg == "1":
        part1()
    if args.pos_arg == "2":
        part2()
    if args.pos_arg == "3":
        part3()


if __name__ == "__main__":
    main()
