#include "lib.h"
#include <cstdlib>
#include <iostream>

std::vector<double> runge_kutta(std::function<double(double, double)> f, int n, double h,
        double x_0, double y_0) {
    double l1, l2, l3, l4, l;

    std::vector<double> iterations;

    double x = x_0;
    double y = y_0;

    for (int i = 0; i < n; ++i) {
        l1 = f(x, y);
        l2 = f(x + h/2.0, y + h/2.0 * l1);
        l3 = f(x + h/2.0, y + h/2.0 * l2);
        l4 = f(x + h, y + h * l3);
        l = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        y += h * l;
        x += h;

        iterations.push_back(y);
    }

    return iterations;
}

std::vector<double> adams_bashford(std::function<double(double, double)> f, int n, double h, 
        double x_0, double y_0) {

    if (n < 4) {
        std::cerr << "Can't use method with less than 4 steps" << std::endl;
        exit(1);
    }

    std::vector<double> iterations;

    double x = x_0;
    double y = y_0;

    // нам нужно будет посчитать 3 значения функии до того, как сможем применить метод Адамса
    const int runge_kutta_steps = 3; 
    
    std::vector<double> prev_values = runge_kutta(f, runge_kutta_steps, h, x, y);
    double y1 = prev_values[0];
    double y2 = prev_values[1];
    double y3 = prev_values[2];
    double f0 = f(x, y);
    double f1 = f(x + h, y1);
    double f2 = f(x + h * 2.0, y2);
    double f3 = f(x + h * 3.0, y3);
    
    x += 3.0 * h;

    for (int i = 3; i < n; ++i) {
        y = y3 + h * (55.0*f3 - 59.0*f2 + 37*f1 - 9*f0) / 24.0;
        x += h;

        y3 = y;
        f0 = f1;
        f1 = f2;
        f2 = f3;
        f3 = f(x, y);
        iterations.push_back(y);
    }

    return iterations;
}

std::vector<std::vector<double>> runge_kutta_2(
        std::function<double(double, double, double)> f,
        double x0, double y0, double y_prime0,
        double h, int n_steps) {

    std::vector<double> x(n_steps + 1);
    std::vector<double> y(n_steps + 1);
    std::vector<double> y_prime(n_steps + 1);

    x[0] = x0;
    y[0] = y0;
    y_prime[0] = y_prime0;

    for (int i = 0; i < n_steps; ++i) {
        double k1_y = y_prime[i];
        double k1_v = f(x[i], y[i], y_prime[i]);

        double k2_y = y_prime[i] + 0.5 * h * k1_v;
        double k2_v = f(x[i]+0.5*h, y[i]+0.5*h*k1_y, y_prime[i]+0.5*h*k1_v);

        double k3_y = y_prime[i] + 0.5 * h * k2_v;
        double k3_v = f(x[i]+0.5*h, y[i]+0.5*h*k2_y, y_prime[i]+0.5*h*k2_v);

        double k4_y = y_prime[i] + h * k3_v;
        double k4_v = f(x[i]+h, y[i]+h*k3_y, y_prime[i]+h*k3_v);

        y[i+1] = y[i] + (h / 6.0) * (k1_y + 2*k2_y + 2*k3_y + k4_y);
        y_prime[i+1] = y_prime[i] + (h / 6.0) * (k1_v + 2*k2_v + 2*k3_v + k4_v);
        x[i+1] = x[i] + h;
    }

    return {x, y, y_prime};
}

std::vector<std::vector<double>> adams_bashforth_2(
    std::function<double(double, double, double)> f,
    double x0, double x_end, double y0, double y_prime0,
    double h) {

    std::vector<std::vector<double>> rk_result = runge_kutta_2(f, x0, y0, y_prime0, h, 3);
    std::vector<double> x_rk = rk_result[0];
    std::vector<double> y_rk = rk_result[1];
    std::vector<double> y_prime_rk = rk_result[2];

    int n = static_cast<int>((x_end - x0) / h) + 1;
    std::vector<double> x(n);
    std::vector<double> y(n);
    std::vector<double> y_prime(n);

    for (int i = 0; i < 4; ++i) {
        x[i] = x_rk[i];
        y[i] = y_rk[i];
        y_prime[i] = y_prime_rk[i];
    }

    for (int i = 3; i < n-1; ++i) {
        y[i+1] = y[i] + h/24.0 * (
            55.0 * y_prime[i] -
            59.0 * y_prime[i-1] +
            37.0 * y_prime[i-2] -
            9.0 * y_prime[i-3]
        );

        y_prime[i+1] = y_prime[i] + h/24.0 * (
            55.0 * f(x[i], y[i], y_prime[i]) -
            59.0 * f(x[i-1], y[i-1], y_prime[i-1]) +
            37.0 * f(x[i-2], y[i-2], y_prime[i-2]) -
            9.0 * f(x[i-3], y[i-3], y_prime[i-3])
        );

        x[i+1] = x[i] + h;
    }

    return {x, y, y_prime};
}
