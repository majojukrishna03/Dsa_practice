'''
Need to print the sub arrays in new lines

'''


# Using normal way
a = [1,2,3,4]
for i in range(len(a)):
    b = []
    for j in range(i,len(a)):
        b.append((a[j]))
        print(b)
    print()




# using * before the array we are printing
a = [1,2,3,4]
for i in range(len(a)):
    b = []
    for j in range(i,len(a)):
        b.append((a[j]))
        print(*b)






# using str .join method

a = [1,2,3,4]
for i in range(len(a)):
    b = []
    for j in range(i,len(a)):
        b.append(str(a[j]))
        # print(*b)
        print(" ".join(b))
    # print()