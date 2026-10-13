def matrix_transpose(m):
    return [[m[i][j] for j in range(len(m[0]))] for i in range(len(m))]
