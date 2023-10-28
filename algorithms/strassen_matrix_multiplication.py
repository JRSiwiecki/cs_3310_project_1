from utilities.utils import print_matrix, combine_submatrices_horizontally, combine_submatrices_vertically, partition_matrix, add_matrices, subtract_matrices

def strassen_matrix_multiplication(a, b):
    matrix_length = len(a) 

    # base case
    if matrix_length == 2:
        c11 = [(a[0][0] * b[0][0]) + (a[0][1] * b[1][0])]
        c12 = [(a[0][0] * b[0][1]) + (a[0][1] * b[1][1])]
        c21 = [(a[1][0] * b[0][0]) + (a[1][1] * b[1][0])]
        c22 = [(a[1][0] * b[0][1]) + (a[1][1] * b[1][1])]

    # otherwise calculate strassen equations
    else:

        a11, a12, a21, a22 = partition_matrix(a)
        b11, b12, b21, b22 = partition_matrix(b)

        p = strassen_matrix_multiplication(add_matrices(a11, a22), add_matrices(b11, b22))
        q = strassen_matrix_multiplication(add_matrices(a21, a22), b11)
        r = strassen_matrix_multiplication(a11, subtract_matrices(b12, b22))
        s = strassen_matrix_multiplication(a22, subtract_matrices(b21, b11))
        t = strassen_matrix_multiplication(add_matrices(a11, a12), b22)
        u = strassen_matrix_multiplication(subtract_matrices(a21, a11), add_matrices(b11, b12))
        v = strassen_matrix_multiplication(subtract_matrices(a12, a22), add_matrices(b21, b22))
        
        c11 = add_matrices(p, add_matrices(subtract_matrices(s, t), v))
        c12 = add_matrices(r, t)
        c21 = add_matrices(q, s)
        c22 = add_matrices(p, add_matrices(subtract_matrices(r, q), u))
    
    c1 = combine_submatrices_horizontally(c11, c12)
    c2 = combine_submatrices_horizontally(c21, c22)

    c = combine_submatrices_vertically(c1, c2)

    return c