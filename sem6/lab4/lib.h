#ifndef LIB_H

#include <functional>
#include <vector>

std::vector<double> runge_kutta(std::function<double(double, double)> f, int n, double h, 
        double x_0, double y_0);

std::vector<double> adams_bashford(std::function<double(double, double)> f, int n, double h, 
        double x_0, double y_0);

std::vector<std::vector<double>> runge_kutta_2(
        std::function<double(double, double, double)> f,
        double x0, double y0, double y_prime0,
        double h, int n_steps);

std::vector<std::vector<double>> adams_bashforth_2(
    std::function<double(double, double, double)> f,
    double t0, double t_end, double y0, double y_prime0,
    double h);

#endif // !LIB_H
