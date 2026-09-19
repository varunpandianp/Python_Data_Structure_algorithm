n=int(input())
row=1
while row<=n:
    j=1
    space=1
    while space <= n-row:
        print(" ",end="")
        space=space+1
    #increasingpart
    while j<=row:
        print(j,end="")
        j=j+1
    #decresingpart
    num=row-1
    while num >=1:
        print(num,end="")
        num=num-1
    row=row+1
    print()