def bubbleSort(arr,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# test case 1: 
arr1 = [5,1,3,7,2]
n1 = len(arr1)

print(bubbleSort(arr1,n1))

print("-------------------------------------------------------------")

# test case 2: 
arr2 = [100,121,92,10,15]
n2 = len(arr2)

print(bubbleSort(arr2,n2))

print("-------------------------------------------------------------")

# test case 3: 
arr3 = [54,1,38,57,21]
n3 = len(arr3)

print(bubbleSort(arr3,n3))

print("-------------------------------------------------------------")
