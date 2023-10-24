from utilities.utils import partition_matrix, add_matrices, combine_submatrices_horizontally, combine_submatrices_vertically

def divide_and_conquer_matrix_multiplication(a, b):
    matrix_length = len(a) 

    # base case
    if matrix_length == 1:
        return [a[0][0] * b[0][0]]
    
    # partition matrices into 4 submatrices if base case is not met
    a11, a12, a21, a22 = partition_matrix(a)

    b11, b12, b21, b22 = partition_matrix(b)

    c11 = add_matrices(
        divide_and_conquer_matrix_multiplication(a11, b11),
        divide_and_conquer_matrix_multiplication(a12, b21)
    )

    c12 = add_matrices(
        divide_and_conquer_matrix_multiplication(a11, b12),
        divide_and_conquer_matrix_multiplication(a12, b22)
    )

    c21 = add_matrices(
        divide_and_conquer_matrix_multiplication(a21, b11),
        divide_and_conquer_matrix_multiplication(a22, b21)
    )

    c22 = add_matrices(
        divide_and_conquer_matrix_multiplication(a21, b12),
        divide_and_conquer_matrix_multiplication(a22, b22)
    )

    c1 = combine_submatrices_horizontally(c11, c12)
    c2 = combine_submatrices_horizontally(c21, c22)

    c = combine_submatrices_vertically(c1, c2)

    return c