# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 5
#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines

N=int(input())

for i in range(0,N,2):
    for j in range(1,N+1):
        print(i*N+j,end=" ")
    print()
if N % 2 == 0:
    start = N - 1
else:
    start = N - 2

for i in range(start,-1,-2):
    for j in range(1,N+1):
        print(i*N+j,end=" ")
    print()