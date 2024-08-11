def largestElement(arr):
    # code1
    if len(arr) == 0:
        return "Empty"
    return max(arr)

def maxElement(arr,n):
    if len(arr) == 0: 
        return "Empty"
    l = arr[0]
    m = 0
    while(m<n):
        if arr[m]>l:
            l = arr[m]
        m+=1
    return l



# Testcases :
arr1 = [1,3,4,9,5]
arr2 = [5,5,5,5,5]
arr3 = [10]
arr4 = []

print("Using max: ")
print()
print("arr1")
print(largestElement(arr1))
print("----------------------")
print()

print("arr2")
print(largestElement(arr2))
print("----------------------")
print()

print("arr3")
print(largestElement(arr3))
print("----------------------")
print()

print("arr4")
print(largestElement(arr4))
print("----------------------")
print()

print("Using iteration: ")
print()

print("arr1")
print(maxElement(arr1,5))
print("----------------------")
print()

print("arr2")
print(maxElement(arr2,5))
print("----------------------")
print()

print("arr3")
print(maxElement(arr3,1))
print("----------------------")
print()

print("arr4")
print(maxElement(arr4,0))
print("----------------------")
print()