import random

# n is n*n size of matrices
# range is list containing 2 numbers, min and max
def generate_random_matrices(matrix_size, number_range):
    MIN_VALUE, MAX_VALUE = number_range

    a = generate_blank_matrix(matrix_size)
    b = generate_blank_matrix(matrix_size)
    
    for row in range(0, len(a)):
        for col in range(0, len(a[row])):
            a[row][col] = random.randint(MIN_VALUE, MAX_VALUE)
            b[row][col] = random.randint(MIN_VALUE, MAX_VALUE)
    
    return [a, b]

def print_matrix(matrix):
    for row in range(len(matrix)):
        print("[", end="")
        for col in range(len(matrix[row])):
            if col == len(matrix[row]) - 1:
                print(matrix[row][col], end="")
            else:
                print(matrix[row][col], end=" ")
        if row == len(matrix) - 1:
            print("]")
        else:
            print("],")
        
    print("")

def generate_blank_matrix(matrix_size):
    matrix = []

    for i in range(0, matrix_size):
        matrix.append([0] * matrix_size)
    
    return matrix