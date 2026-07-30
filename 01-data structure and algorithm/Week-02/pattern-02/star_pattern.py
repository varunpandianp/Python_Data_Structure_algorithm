# Problem statement
# Print the following pattern
#
# Pattern for N = 4
#

N = int(input())

i=1
while i <= N:
    j=1
    space = 1
    while space <= N-i:
        print(" ",end="")
        space=space+1
    p=1
    while p <=i:
        print("*",end="")
        p=p+1
    p = i - 1
    while p >= 1:
        print("*",end="")
        p=p-1
    print()
    i = i+1

