from classical_matrix_multiplication import classical_matrix_multiplication
from utils import generate_random_matrices, print_matrix

n = 3
min = 0
max = 5

a, b = generate_random_matrices(n, [min, max])
print_matrix(a)
print_matrix(b)
print_matrix(classical_matrix_multiplication(a, b))