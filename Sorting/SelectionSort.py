def selectionSort(arr,n):
    for i in range(n-1):
        m = i
        for j in range(i+1,n):
            if arr[j] < arr[m]:
                m = j
        arr[m],arr[i] = arr[i], arr[m]
    return arr

# test case 1: 
arr1 = [5,1,3,7,2]
n1 = len(arr1)

print(selectionSort(arr1,n1))

print("-------------------------------------------------------------")

# test case 2: 
arr2 = [100,121,92,10,15]
n2 = len(arr2)

print(selectionSort(arr2,n2))

print("-------------------------------------------------------------")

# test case 3: 
arr3 = [54,1,38,57,21]
n3 = len(arr3)

print(selectionSort(arr3,n3))

print("-------------------------------------------------------------")
