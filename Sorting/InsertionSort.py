def insertionSort(alist, n):
        #code here
        for i in range(n):
            k = alist[i]
            j = i-1
            
            while j >=0 and k < alist[j]:
                alist[j+1] = alist[j]
                j-=1
            alist[j+1] = k

        return alist
# testcase 1:
print(insertionSort(alist=[5,3,9,1,2],n=5))
print("-------------------")

#  testcase 2:
print(insertionSort(alist=[10,50,33,61,100],n=5))
print("-------------------")

# testcase 3: 
print(insertionSort(alist=[0,99,82,15,37],n=5))
print("-------------------")

        