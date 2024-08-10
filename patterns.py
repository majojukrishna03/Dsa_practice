# Pattern 1
'''
* * *
* * *
* * *
'''
def pattern1(n):
    print("Pattern 1")
    for i in range(n):
        print("* "*n)

pattern1(5)
print()
print("----------------------------------")

# Pattern 2
'''
* 
* *
* * *
'''
def pattern2(n):
    print("Pattern 2")
    for i in range(1,n+1):
        print("* "*i)

pattern2(5)
print()
print("----------------------------------")

# Pattern 3
''' 
1
1 2 
1 2 3
'''
def pattern3(n):
    print("Pattern 3")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


pattern3(5)
print()
print("----------------------------------")