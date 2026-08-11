# Problem statement
# Print the following pattern for the given number of rows.
#
# Note: N is always odd.
#
#
# Pattern for N = 5
#
#
#
# The dots represent spaces.

n=int(input())
mid=n//2+1

#print(mid)

for i in range(mid):
    for j in range(mid-1-i):
        print(" ",end="")
    for j in range(2 * i + 1):
            print("*",end="")
    print()
for i in range(mid - 2, -1, -1):
    for j in range(mid-1-i):
        print(" ",end="")
    for j in range(2 * i + 1):
            print("*",end="")
    print()