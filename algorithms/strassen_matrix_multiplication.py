from utilities.utils import combine_submatrices_horizontally, combine_submatrices_vertically, partition_matrix, add_matrices

def strassen_matrix_multiplication(a, b):
    matrix_length = len(a) 

    # base case
    if matrix_length == 2:
        c11 = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0])
        c12 = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1])
        c21 = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0])
        c22 = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1])

    else:

        a11, a12, a21, a22 = partition_matrix(a)
        b11, b12, b21, b22 = partition_matrix(b)

        p = strassen_matrix_multiplication(a11, b11)
        q = strassen_matrix_multiplication(a12, b21)
        r = strassen_matrix_multiplication(a11, b12)
        s = strassen_matrix_multiplication(a12, b22)
        t = strassen_matrix_multiplication(a22, b21)
        u = strassen_matrix_multiplication(a21, b11)
        v = strassen_matrix_multiplication(a22, b12)

        c11 = p + s - t + v
        c12 = r + t
        c21 = q + s
        c22 = p + r - q + u
    
    c1 = combine_submatrices_horizontally(c11, c12)
    c2 = combine_submatrices_horizontally(c21, c22)

    c = combine_submatrices_vertically(c1, c2)

    return c