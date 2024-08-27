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

# Pattern 13
'''
1
2 3
4 5 6
'''
def pattern13(n):
    print("Pattern 13")
    a=1
    for i in range(1,n+1):
        for j in range(i):
            print(a,end=" ")
            a+=1
        print()

pattern13(5)
print()
print("----------------------------------")

# Pattern 14
'''
A
A B
A B C
'''
def pattern14(n):
    print("Pattern 14")
    for i in range(n):
        A=65
        for i in range(i+1):
            print(chr(A),end=" ")
            A+=1
        print()

pattern14(5)
print()
print("----------------------------------")

# Pattern 15
'''
A B C
A B
A
'''
def pattern15(n):
    print("Pattern 15")
    for i in range(n,0,-1):
        A=65
        for i in range(i):
            print(chr(A),end=" ")
            A+=1
        print()

pattern15(5)
print()
print("----------------------------------")

# Pattern 16
'''
A
B B
C C C
'''
def pattern16(n):
    print("Pattern 16")
    A=65
    for i in range(n):
        for i in range(i+1):
            print(chr(A),end=" ")
        print()
        A+=1

pattern16(5)
print()
print("----------------------------------")

# Pattern 17
'''
    A
  A B A
A B C B A
'''
def pattern17(n):
    a = 65  # ASCII value of 'A'
    for i in range(1, n + 1):
        # Calculate leading spaces
        spaces = ' ' * (n - i)
        
        # Generate the pattern for the current row
        pattern = [chr(a + j) for j in range(i)]  # Increasing sequence
        pattern += [chr(a + j) for j in range(i - 2, -1, -1)]  # Decreasing sequence
        
        # Join the pattern list into a string with spaces
        line = ' '.join(pattern)
        
        # Print the line with leading spaces
        print(spaces + line)

pattern17(5)
print()
print("----------------------------------")

# Pattern 18
'''
C
C B
C B A
'''
def pattern18(n):
    # Write your solution here.
    a=65
    start = a+n-1
    for i in range(1,n+1):
        for j in range(i):
            print(chr(start-j),end=" ")
        print()


pattern18(5)
print()
print("----------------------------------")

# pattern 19
'''
1 2 3 4 5 
2 3 4 5 1 
3 4 5 1 2 
4 5 1 2 3 
5 1 2 3 4
'''

def pattern19(n):
    for i in range(1,n+1):
        for j in range(i,i+5):
            if (j%5 !=0) :
                print(j%5, end=" ")
            else:
                print(5,end=" ")
        print()

pattern19(5)
print()
print("----------------------------------")

# pattern20
'''
    1
   21
  321
 4321
54321
'''

def pattern20(n):
    for i in range(1,n+1):
        print(" " * (5-i),end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()

pattern20(5)

