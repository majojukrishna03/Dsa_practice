def print2largest(arr):
    # Code Here
    lar = arr[0]
    secLar = -1
    m = 0
    while(m<len(arr)):
        if arr[m] > lar:
            secLar = lar
            lar = arr[m]
        elif arr[m] > secLar and arr[m] != lar:
            secLar = arr[m]
        m+=1
    return secLar

# testcases 

arr1 = [1,3,4,9,5]
arr2 = [5,5,5,5,5]
arr3 = [10]

print()

print("arr1")
print(print2largest(arr1))
print("----------------------")
print()

print("arr2")
print(print2largest(arr2))
print("----------------------")
print()

print("arr3")
print(print2largest(arr3))
print("----------------------")
print()
