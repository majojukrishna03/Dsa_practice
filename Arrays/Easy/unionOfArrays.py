'''
Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.
'''

#Function to return a list containing the union of the two arrays.
def findUnion(self,arr1,arr2,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    result = []
    i, j = 0, 0
    # Traverse both arrays
    while i < n and j < m:
        # Skip duplicates in arr1
        while i > 0 and i < n and arr1[i] == arr1[i-1]:
            i += 1
        # Skip duplicates in arr2
        while j > 0 and j < m and arr2[j] == arr2[j-1]:
            j += 1
            
        if i < n and j < m:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
    
    # Add remaining elements of arr1
    while i < n:
        if i > 0 and arr1[i] != arr1[i-1]:
            result.append(arr1[i])
        i += 1
    
    # Add remaining elements of arr2
    while j < m:
        if j > 0 and arr2[j] != arr2[j-1]:
            result.append(arr2[j])
        j += 1
    
    return result