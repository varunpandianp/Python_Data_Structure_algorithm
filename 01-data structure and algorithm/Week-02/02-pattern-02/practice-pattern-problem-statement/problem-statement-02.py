n=int(input())
i=1
mid=n//2+1
#print(mid)
while i <= mid:
    j=1
    while j <= mid-i:
        print(" ",end="")
        j=j+1
     #upperleftpart
    value=1
    while value <=i:
        print(value,end="")
        value=value+1
    #upperrightpart
    value = i-1
    while value >=1:
        print(value,end="")
        value=value-1
    print()
    i=i+1
#lowerpart
i=mid-1
while i >=1:
    j=1
    while j <= mid-i:
        print(" ",end="")
        j=j+1
    value=1
    while value <=i:
        print(value,end="")
        value=value+1
        #upperrightpart
    value = i-1
    while value >=1:
        print(value,end="")
        value=value-1
    print()
    i=i-1


