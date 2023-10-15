from classical_matrix_multiplication import classical_matrix_multiplication
from utils import generate_random_matrices, print_matrix

a, b = generate_random_matrices(4, [0, 10])
print_matrix(a)
print_matrix(b)
# print(classical_matrix_multiplication(n, a, b))