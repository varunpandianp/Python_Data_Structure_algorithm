n = int(input("Enter the value:"))

i = 1
while i <=n:
    j=1
    space=1
    while space <= n-i:
        print(" ",end="")
        space=space+1
    p=1
    while j <= i:
        print(p,end="")
        p=p+1
        j=j+1
    p = i - 1
    while p >= 1:
        print(p,end="")
        p=p-1
    print()
    i=i+1