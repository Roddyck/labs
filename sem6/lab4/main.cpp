#include <cassert>
#include <cfloat>
#include <functional>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <string>
#include "lib.h"

double func1(double x, double y) {
    return y - x;
}

double solution1(double x) {
    return 16.0 * std::exp(x) + x + 1;
}

double func2(double x, double y) {
    return y - (2.0*x / y);
}

double solution2(double x) {
    return std::sqrt(1.0 + 2.0 * x + 288.0 * std::exp(2.0 * x));
}

double func3(double x, double y) {
    return (1.0 + std::pow(y, 2) * std::sin(2*x)) / (2*y * std::pow(std::cos(x), 2));
}

double solution3(double x) {
    return std::sqrt(x) / std::cos(x);
}

double func_second_order(double x, double y, double y_prime) {
    return 2.0 * y_prime - y;
}

double solution_second_order(double x) {
    return (7.0 - 3.0 * x) * std::exp(x - 2.0);
}

void test() {
    auto func_test = [](double x, double y) { return x - y; };
    double y_0_test = 2.0;
    double x_0_test = 0.0;
    double h_test = 0.1;
    int n_test = 1;
    const double true_value_test = 1.814513;

    std::vector<double> res_test_runge = runge_kutta(func_test, n_test, h_test, x_0_test, y_0_test);
    assert(std::fabs(res_test_runge[0] - true_value_test) < 5e-5);

    std::cout << "Test passed!" << std::endl;
}

void part1(std::function<double(double,double)> func, std::function<double(double)> sol, 
        const double x_0, const double y_0, const double end) {
    int n = 5;
    double sol_true = sol(end);
    double prev_error = 0.0;
    
    while (n <= 80) {
        double h = (end - x_0) / n;
        std::vector<double> runge_kutta_res = runge_kutta(func, n, h, x_0, y_0);
        double res = runge_kutta_res.back();
        double error = fabs(res - sol_true);

        std::cout << std::setprecision(10) << "Runge Kutta method value, for n = " 
            << n << ": " << res
            << ", Real value in: " << sol_true << std::endl;

        std::cout << "Absolute error = " << error << std::endl;

        if (n > 5) {
            std::cout << "Current error less than previous in " << prev_error / error
                << " times" << std::endl;
        }

        std::cout << std::endl;

        prev_error = error;
        n *= 2;
    }

    n = 5;
    while (n <= 80) {
        double h = (end - x_0) / n;
        std::vector<double> adams_res = adams_bashford(func, n, h, x_0, y_0);
        double res = adams_res.back();
        double error = fabs(res - sol_true);

        std::cout << std::setprecision(10) << "Adams method value in x, for n = " 
            << n << ": " << res
            << ", Real value in: " << sol_true << std::endl;

        std::cout << "Absolute error = " << error << std::endl;

        if (n > 5) {
            std::cout << "Current error less than previous in " << prev_error / error
                << " times" << std::endl;
        }

        std::cout << std::endl;

        prev_error = error;
        n *= 2;
    }
}

void part2(const double eps=1e-8) {
    const double x_0_first = 0.0;
    const double y_0_first = 17.0;
    double sol_true = solution2(1.0);
    int n = 5;
    double abs_error;

    do {
        std::vector<double> runge_kutta_res = runge_kutta(func2, n, 1.0/n, x_0_first, y_0_first);
        double res = runge_kutta_res.back();
        abs_error = std::fabs(res - sol_true);
        n += 1;
    } while (abs_error > eps);
    
    std::cout << "For Runge Kutta method " << n << " steps was needed to get error < "
        << eps << std::endl;

    n = 5;
    do {
        std::vector<double> adams_res = runge_kutta(func2, n, 1.0/n, x_0_first, y_0_first);
        double res = adams_res.back();
        abs_error = std::fabs(res - sol_true);
        n += 1;
    } while (abs_error > eps);
    
    std::cout << "For Adams method " << n << " steps was needed to get error < "
        << eps << std::endl;
}

void part3() {
    double x0 = 2.0;
    double y0 = 1.0;
    double y_prime0 = -2.0;
    double x_end = 3.0;
    std::vector<std::vector<double>> rk_result = runge_kutta_2(func_second_order, x0, y0, y_prime0, 0.1, 10);
    std::cout << "Runge-Kutta result for second order equation" << std::endl;
    std::cout << "x\ty\ty'" << std::endl;
    std::cout << rk_result[0].back() << "\t" << rk_result[1].back() << "\t"
        << rk_result[2].back() << std::endl;
    std::cout << "True value: " << solution_second_order(3.0) << std::endl;
    std::cout << std::setprecision(5)
        << "Absolute error: " << fabs(rk_result[1].back() - solution_second_order(3.0))
        << std::endl;

    std::vector<std::vector<double>> ab_result = adams_bashforth_2(func_second_order, x0, x_end, y0, y_prime0, 0.1);
    std::cout << "\nAdams-Bashford result for second order equation" << std::endl;
    std::cout << "x\ty\ty'" << std::endl;
    std::cout << ab_result[0].back() << "\t" << ab_result[1].back() << "\t"
        << ab_result[2].back() << std::endl;
    std::cout << "True value: " << solution_second_order(3.0) << std::endl;
    std::cout << std::setprecision(5)
        << "Absolute error: " << fabs(ab_result[1].back() - solution_second_order(3.0))
        << std::endl;
}

int main(int argc, char *argv[]) {
    const double x_0_first = 0.0;
    const double y_0_first = 17.0;
    const double x_0_second = M_PI;
    const double y_0_second = -std::sqrt(M_PI);
    const double end_third = (3.0 * M_PI) / 2.0;

    if (argc != 2) {
        std::cerr << "You should pass one argument (part of task [1-3])";
        exit(1);
    }

    if (std::string(argv[1]) == "1") {
        std::cout << "First function" << std::endl; 
        part1(func1, solution1, x_0_first, y_0_first, 1.0);
        std::cout << "Second function" << std::endl; 
        part1(func2, solution2, x_0_first, y_0_first, 1.0);
        std::cout << "Third function" << std::endl;
        part1(func1, solution3, x_0_second, y_0_second, end_third);

    }

    if (std::string(argv[1]) == "2") {
        part2();
    }

    if (std::string(argv[1]) == "3") {
        part3();
    }

    return 0;
}
