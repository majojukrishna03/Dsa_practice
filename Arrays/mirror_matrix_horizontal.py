
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def mirror_matrix_horizontal(matrix):
    res = []
    for i in range(len(matrix)-1,-1,-1):
        res.append(matrix[i])
    return res

print(mirror_matrix_horizontal(matrix))