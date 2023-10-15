def classical_matrix_multiplication(n, a, b):
    c = [[0 * n], [0 * n]]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c