# Problem statement
# Print the following pattern
#
# Pattern for N = 4
#
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

N=int(input())
i=1
while i <=N:
    j=1
    while j<=2*N+1:
        if j==i or j==N+1 or j ==(2*N+2-i):
            print("*",end="")
        else:
            print(0,end="")
        j=j+1
    print()
    i=i+1