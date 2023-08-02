def transponse(matrix):
    result = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Исходная матрица: {mat}')
print(f'Транспонированная матрица: {transponse(mat)}')
