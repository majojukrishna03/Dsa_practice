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

# Pattern 8
'''
*****
 ***
  *
'''   
def pattern8(n):
    print("Pattern 8")
    for i in range(n,0,-1):
        print(" "*(n-i) +"*"*(2*i-1))

pattern8(5)
print()
print("----------------------------------")

# Pattern 9
'''
  *
 ***
*****
*****
 ***
  *
'''
def pattern9(n):
    print("Pattern 9")
    for i in range(n):
        print(" "*(n-i-1)+"*"*(i*2+1)+" "*(n-i-1))
    for i in range(n,0,-1):
        print(" "*(n-i) +"*"*(2*i-1))

pattern9(5)
print()
print("----------------------------------")

# Pattern 10
'''
*
**
***
**
*
'''
def pattern10(n):
    print("Pattern 10")
    for i in range(1,n):
        print("*"*i)
    for i in range(n,0,-1):
        print("*"*i)

pattern10(5)
print()
print("----------------------------------")

# Pattern 11
'''
1
0 1
1 0 1
'''
def pattern11(n):
    print("Pattern 11")
    for i in range(n):
        for j in range(i+1):
            print((i+j+1)%2,end=" ")
        print()

pattern11(5)
print()
print("----------------------------------")

# Pattern 12
'''
1         1
1 2     2 1
1 2 3 3 2 1
'''
def pattern12(n):
    print("Pattern 12")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range((n-i)*2):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

pattern12(5)
print()
print("----------------------------------")

