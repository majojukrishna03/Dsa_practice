matrix = [[1,2,3],[4,5,6],[7,8,9]]

'approach-1'

# def reverse(lst):
#     res = []
#     for i in range(len(lst)-1,-1,-1):
#         res.append(lst[i])
#     return res

# # print(reverse([4,5,6]))

# def snake_pattern(matrix):
#     res = []
#     for i in range(len(matrix)):
#         sub = []
#         for j in range(len(matrix[i])):
#             sub.append(matrix[i][j])
#         if i % 2 == 0:
#             res.append(sub)
#         else: 
#             # rev = list(reversed(sub))
#             # print(rev)
#             rev = reverse(sub)
#             res.append(rev)
#     return res

# print(snake_pattern(matrix))

'approach-2'

def snake_pattern(matrix):
    res = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            res.append(matrix[i])
        else: 
            res.append(matrix[i][::-1])
    return res

print(snake_pattern(matrix))