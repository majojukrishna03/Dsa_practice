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

# Pattern 4
'''
1 
2 2 
3 3 3
'''   
def pattern4(n):
    print("Pattern 4")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end = " ")
        print()


pattern4(5)
print()
print("----------------------------------")

# Pattern 5
'''
* * *
* *
*
'''   

def pattern5(n):
    print("Pattern 5")
    for i in range(n,0,-1):
        print("* "*i)


pattern5(5)
print()
print("----------------------------------")


# Pattern 6
'''
1 2 3
1 2
1
'''   

def pattern6(n):
    print("Pattern 6")
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()


pattern6(5)
print()
print("----------------------------------")

# Pattern 7
'''
  *
 ***
*****
'''   
def pattern7(n):
    print("Pattern 7")
    for i in range(n):
        print(" "*(n-i-1)+"*"*((i*2)+1)+" "*(n-i-1))

pattern7(5)
print()
print("----------------------------------")