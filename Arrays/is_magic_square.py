'''
magic square is a matrix if sum of all rows,cols and diagonals is same.
'''

matrix =  [[1,2,3],[4,5,6],[7,8,9]]


def is_sum_rows(matrix):
    is_all_rows = True
    sum_ = []
    sum_1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum_1 += matrix[i][j]
        if len(sum_) == 0:
            sum_.append(sum_1)
        else: 
            if i > 0 and sum_[i-1] != sum_1:
                is_all_rows = False
            sum_.append(sum_1)
        sum_1 = 0
    # print(sum_)
    return is_all_rows 
    
# print(sum_rows(matrix))

def is_sum_cols(matrix):
    is_all_cols = True
    sum_ = []
    sum_1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum_1 += matrix[j][i]
        if len(sum_) == 0:
            sum_.append(sum_1)
        else: 
            if i > 0 and sum_[i-1] != sum_1:
                is_all_cols = False
            sum_.append(sum_1)
        sum_1 = 0
    # print(sum_)
    return is_all_cols 
    
# print(sum_cols(matrix))

def is_sum_diagonals(matrix):
    is_both_diagonals = True
    sum_1 = 0
    sum_2 = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i==j:
                sum_1 += matrix[i][i]
    
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[i])-1,-1,-1):
            if i==j:
                sum_2 += matrix[i][j]
    
    if sum_1 != sum_2:
        is_both_diagonals = False
    # print(sum_1,sum_2)
    return is_both_diagonals

# print(is_sum_diagonals(matrix))
    
def magic_square(matrix):
    is_magic_square = True
    if is_sum_rows(matrix):
        if is_sum_cols(matrix):
            if is_sum_diagonals(matrix):
                return is_magic_square
            else: 
                is_magic_square = False
        else: 
            is_magic_square = False
    else: 
        is_magic_square = False
    return is_magic_square

print(magic_square(matrix))