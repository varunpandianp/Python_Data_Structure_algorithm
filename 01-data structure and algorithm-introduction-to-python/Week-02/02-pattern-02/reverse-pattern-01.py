n=int(input())
i = 1
while i <= n:
    j=1
    space=1
    while j <=n:
        if j <= n-i:
            print(" ",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1
    print()