# Problem statement
# Print the following pattern for n number of rows.
#
# Note: each line consist of equal number of characters +
# spaces. Suppose you are printing xth line for N=n.
# You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1

n=int(input())
i=1
while i <= n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    space = 1
    while space <= 2*(n-i):
        print(" ",end="")
        space=space+1
    j=i
    while j >=1:
        print(j,end="")
        j=j-1
    print()
    i=i+1

