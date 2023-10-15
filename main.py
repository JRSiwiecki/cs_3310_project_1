from utilities.utils import generate_random_matrices, print_matrix
from algorithms.classical_matrix_multiplication import classical_matrix_multiplication

N = 3
MIN = 0
MAX = 5

a, b = generate_random_matrices(N, [MIN, MAX])

print("MATRIX A:\n")
print_matrix(a)

print("MATRIX B:\n")
print_matrix(b)

print("----- CLASSICAL MATRIX MULTIPLICATION -----\n")
print_matrix(classical_matrix_multiplication(a, b))
print("-------------------------------------------")

# print("----- DIVIDE AND CONQUER MATRIX MULTIPLICATION -----\n")
# print_matrix(divide_and_conquer_matrix_multiplication(a, b))
# print("------------------------------------------------------")

# print("----- STRASSEN MATRIX MULTIPLICATION -----\n")
# print_matrix(strassen_matrix_multiplication(a, b))
# print("--------------------------------------------")