n=int(input())
i=1
while i <= n:
    j=1

    while j <= n-i:
        print(" ",end="")
        j=j+1
    star=1
    while star <= 2*i -1:
        print("*",end="")
        star=star+1
    print()
    i=i+1