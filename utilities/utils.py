import random
import numpy
import time

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

# prints matrix somewhat nicely
def print_matrix(matrix):
    for row in range(len(matrix)):
        print("[", end="")
        for col in range(len(matrix[row])):
            if col == len(matrix[row]) - 1:
                print(matrix[row][col], end="")
            else:
                print(matrix[row][col], end=", ")
        print("]")
        
    print("")

# creates blank matrix to be used for generating random matrices
def generate_blank_matrix(matrix_size):
    matrix = []

    for i in range(0, matrix_size):
        matrix.append([0] * matrix_size)
    
    return matrix

# breaks down matrix into 4 submatrices
def partition_matrix(matrix):
    matrix_length = len(matrix)
    
    midpoint = matrix_length // 2

    m11 = [row[:midpoint] for row in matrix[:midpoint]]
    m12 = [row[midpoint:] for row in matrix[:midpoint]]
    m21 = [row[:midpoint] for row in matrix[midpoint:]]
    m22 = [row[midpoint:] for row in matrix[midpoint:]]

    return m11, m12, m21, m22

def add_matrices(a, b):
    if len(a) == 1 and len(b) == 1:
        return [a[0] + b[0]]
    
    c = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        c.append(row)
    
    return c

def subtract_matrices(a,b):
    if len(a) == 1 and len(b) == 1:
        return [a[0] - b[0]]
    
    c = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] - b[i][j])
        c.append(row)
    
    return c

def combine_submatrices_horizontally(a, b): 
    return numpy.hstack((a, b))

def combine_submatrices_vertically(a, b):
    return numpy.vstack((a, b))

# times a given algorithm and returns the algorithm result and its execution time
def time_algorithm(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time