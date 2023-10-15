from utilities.utils import generate_blank_matrix

def classical_matrix_multiplication(a, b):
    n = len(a)
    
    c = generate_blank_matrix(n)
    
    for i in range(0, len(c)):
        for j in range(0, len(c[i])):
            for k in range(0, len(c[i])):
                c[i][j] += a[i][k] * b[k][j]

    return c