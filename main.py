from utilities.utils import generate_random_matrices, print_matrix, time_function
from algorithms.classical_matrix_multiplication import classical_matrix_multiplication
from algorithms.divide_and_conquer_matrix_multiplication import divide_and_conquer_matrix_multiplication
from algorithms.strassen_matrix_multiplication import strassen_matrix_multiplication

N = 32
MIN = 1
MAX = 10

a, b = generate_random_matrices(N, [MIN, MAX])

print("MATRIX A:\n")
print_matrix(a)

print("MATRIX B:\n")
print_matrix(b)

algorithms = [classical_matrix_multiplication, 
              divide_and_conquer_matrix_multiplication, 
              strassen_matrix_multiplication]

for algorithm in algorithms:
    print(f"----- {algorithm.__name__.upper()} -----\n")
    result, execution_time = time_function(algorithm, a, b)
    print_matrix(result)
    print(f"Execution Time: {execution_time:.6f} seconds")
    print("-------------------------------------------\n")

print("----- CLASSICAL MATRIX MULTIPLICATION -----\n")
print_matrix(classical_matrix_multiplication(a, b))
print("-------------------------------------------\n")

print("----- DIVIDE AND CONQUER MATRIX MULTIPLICATION -----\n")
print_matrix(divide_and_conquer_matrix_multiplication(a, b))
print("------------------------------------------------------\n")

print("----- STRASSEN MATRIX MULTIPLICATION -----\n")
# print_matrix(strassen_matrix_multiplication(a, b))
print("--------------------------------------------\n")