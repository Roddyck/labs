#include <cmath>
#include <iostream>
#include <fstream>
#include <string>

void read_input(float** matrix, std::string filename, const int& size) {
    std::ifstream file(filename);

    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            file >> matrix[i][j];
        }
    }

    file.close();
}

void print_matrix(float** matrix, const int& size) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

void print_vector(float* vector, const int& size) {
    for (int i = 0; i < size; ++i) {
        std::cout << vector[i] << " ";
    }
    std::cout << std::endl;
}

float* calc_right_side(float** matrix, float* x, const int& size) {
    float* right_side = new float[size];
    
    // естественно в первый раз я забыл это сделать;
    for (int i = 0; i < size; ++i) {
        right_side[i] = 0;
    }

    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            right_side[i] += matrix[i][j] * x[j];
        }
    }

    return right_side;
}

void transform(float** matrix, float* right_side, const int& size) {
    float aii;
    for (int i = 0; i < size; ++i) {
        aii = matrix[i][i];
        right_side[i] /= aii;
        for (int j = 0; j < size; ++j) {
            matrix[i][j] /= aii;
        }
    }
}

float matrix_norm(float** matrix, const int& size) {
    float norm = -1.;
    float cur_sum = 0.;

    for (int i = 0; i < size; ++i) {
        cur_sum = 0;
        for (int j = 0; j < size; ++j) {
            cur_sum += fabs(matrix[i][j]);
        }

        if (cur_sum > norm) {
            norm = cur_sum;
        }
    }

    return norm;
}

void jacobi_method(float** matrix, float* right_side, float x_approx[], const int& size, float epsilon) {
    float delta[size];
    float tempX[size];
    float error; 
    
    int count = 0;

    for (int i = 0; i < size; ++i) {
        tempX[i] = x_approx[i];
    }

    do {
        for (int i = 0; i < size; ++i) {
            delta[i] = right_side[i];
            for (int j = 0; j < size; ++j) {
                delta[i] -= matrix[i][j] * x_approx[j];
            }
        }

        for (int i = 0; i < size; ++i) {
            tempX[i] += delta[i];
        }

        error = fabs(x_approx[0] - tempX[0]);
        for (int i = 0; i < size; ++i) {
            if (fabs(x_approx[i] - tempX[i]) > error) {
                error = fabs(x_approx[i] - tempX[i]);
            }
            x_approx[i] = tempX[i];
        }
        count++;
    } while (error > epsilon);

    std::cout << "Number of iterations = " << count << std::endl;
}

void seidel_method(float** matrix, float* right_side, float x_approx[], const int& size, float epsilon) {
    float delta[size];
    float old_x[size];
    float sigma;
    float error; 
    int count = 0;


    do {
        for (int i = 0; i < size; ++i) {
            old_x[i] = x_approx[i];
        }

        for (int i = 0; i < size; ++i) {
            delta[i] = right_side[i];
            sigma = 0;
            for (int j = 0; j < size; ++j) {
                sigma += matrix[i][j] * x_approx[j];
            }

            delta[i] -= sigma;
            x_approx[i] += delta[i];
        }

        error = fabs(x_approx[0] - old_x[0]);
        for (int i = 0; i < size; ++i) {
            if (fabs(x_approx[i] - old_x[i]) > error) {
                error = fabs(x_approx[i] - old_x[i]);
            }
        }
        count++;
    } while (error > epsilon);

    std::cout << "Number of iterations = " << count << std::endl;
}

float calc_stop_case(float norm, float e) {
    float res = (1 - norm) / norm * e;

    return res;
}

int main() {
    const int size = 5;
    float x[] = {1., 9., 3., 6., 5.};
    float* right_side = new float[size];
    float x_approx[size];
    float epsilon[] = {10e-3, 10e-4, 10e-5};

    float** matrix = new float*[size];
    for (int i = 0; i < size; ++i) {
        matrix[i] = new float[size];
    }

    read_input(matrix, "input", size);
    float norm = matrix_norm(matrix, size);

    right_side = calc_right_side(matrix, x, size);

    transform(matrix, right_side, size);
    std::cout << "Norm = " << norm << std::endl;

    for (int i = 0; i < size; ++i) {
        x_approx[i] = right_side[i];
    }

    std::cout << "Jacobi method" << std::endl;
    for (int i = 0; i < sizeof(epsilon) / sizeof(float); ++i) {
        float x_approx_copy[size];

        // Копируем вектор начальных приблежений, чтобы не передавать уже 
        // подсчитание значения в функцию для следующего значения epsilon
        for (int k = 0; k < size; ++k) {
            x_approx_copy[k] = x_approx[k];
        }

        float stop_case = calc_stop_case(norm, epsilon[i]); // смотреть формулу для epsilon_1
        jacobi_method(matrix, right_side, x_approx_copy, size, stop_case);
        std::cout << "X approximation for e = " << epsilon[i] << std::endl;
        print_vector(x_approx_copy, size);
    }


    std::cout << std::endl;
    std::cout << "Seidel method" << std::endl;
    for (int i = 0; i < sizeof(epsilon) / sizeof(float); ++i) {
        float x_approx_copy[size];
        for (int k = 0; k < size; ++k) {
            x_approx_copy[k] = x_approx[k];
        }

        float stop_case = calc_stop_case(norm, epsilon[i]); // смотреть формулу для epsilon_1
        seidel_method(matrix, right_side, x_approx_copy, size, stop_case);
        std::cout << "X approximation for e = " << epsilon[i] << std::endl;
        print_vector(x_approx_copy, size);
    }

    // clean up (unnecessary)
    delete[] right_side;
    for (int i = 0; i < size; ++i) {
        delete[] matrix[i];
    }
    delete[] matrix;
    return 0;
}
