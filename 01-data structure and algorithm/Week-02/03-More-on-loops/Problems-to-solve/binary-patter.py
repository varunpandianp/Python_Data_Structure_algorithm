# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 4
# 1111
# 000
# 11
# 0
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines

n=int(input())
row=1
for i in range(n,0,-1):
    for j in range(i):
        if row % 2 ==1:
            print(1,end="")
        else:
            print(0,end="")
    print()
    row=row+1


