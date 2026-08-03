# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234
# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines

N= int(input())
i=1
while i <= N:
    space=1
    while space <= N-i:
        print(" ",end="")
        space=space+1
     #Leftside
    j=i
    while j >= 1:
        print(j,end="")
        j=j-1
     #rightside
    j=2
    while j <=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1
