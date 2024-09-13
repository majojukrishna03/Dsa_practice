'''
Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
'''
def pascal_Triangle(numRows):
    a = [[1]]
    b = a[len(a)-1]
    for i in range(1,numRows):
        c = [1]
        for j in range(len(b)-1):
            c.append(b[j]+b[j+1])
        c.append(1)
        a.append(c)
        b=c
    return a



# Input
numRows = 5
# Expected Output
# [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

print(pascal_Triangle(numRows))
    