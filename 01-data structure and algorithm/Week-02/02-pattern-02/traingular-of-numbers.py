# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 4
#
#
#
# The dots represent spaces.


N =int(input())
i=1
while i<=N:
    space=1
    while space<=N-i:
        print(" ",end="")
        space=space+1
    j=1
    v=i
    while j<=i:
        print(v,end="")
        v=v+1
        j=j+1
    p=v-2
    while p >= i:
        print(p,end="")
        p=p-1
    print()
    i=i+1