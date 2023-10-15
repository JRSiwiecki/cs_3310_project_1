from utils import generate_random_matrices, print_matrix
from classical_matrix_multiplication import classical_matrix_multiplication

N = 3
MIN = 0
MAX = 5

a, b = generate_random_matrices(N, [MIN, MAX])

print_matrix(a)
print_matrix(b)

print_matrix(classical_matrix_multiplication(a, b))
# print_matrix(divide_and_conquer_matrix_multiplication(a, b))
# print_matrix(strassen_matrix_multiplication(a, b))