#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

#above is the pattern to solve

n=int(input())
i=1
mid=n//2+1

#upperhalf

while i<=mid:
    j=1
    while j<=mid-i:
        print(" ",end="")
        j=j+1
    value=1
    while value <= 2*i-1:
        print("*",end="")
        value=value+1
    i=i+1
    print()
i=mid-1
while i >=1:
    j=1
    while j<=mid-i:
        print(" ",end="")
        j=j+1
    value =1
    while value <= 2*i-1:
        print("*",end="")
        value=value+1
    print()
    i=i-1