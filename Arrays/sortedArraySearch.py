'''
Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.
'''

def searchInSorted(arr, N, K):
    #Your code here
    for i in range(N):
        if arr[i] == K:
            return 1
    return -1

# Test Case 1: Element Present in the Middle of the Array
arr1 = [1, 2, 3, 4, 6]
N1 = 5
K1 = 3
# Expected Output: 1
print(searchInSorted(arr1, N1, K1))  # Output: 1

# Test Case 2: Element Not Present in the Array
arr2 = [1, 3, 4, 5, 6]
N2 = 5
K2 = 2
# Expected Output: -1
print(searchInSorted(arr2, N2, K2))  # Output: -1

# Test Case 3: Element Present at the Beginning of the Array
arr3 = [7, 8, 9, 10, 11]
N3 = 5
K3 = 7
# Expected Output: 1
print(searchInSorted(arr3, N3, K3))  # Output: 1
