n=int(input())
i=1
mid=n//2+1
#upperhalf
while i <= mid:
    j=1
    #leftspace
    while j <=i-1:
        print(" ",end="")
        j=j+1
    #leftnumber
    print(i,end="")

    #middlespace
    middlespace=1
    while middlespace <= 2*(mid-i):
        print(" ",end="")
        middlespace=middlespace+1

#     #middlevalue
#     middlevalue=i
#     if middlevalue==mid:
#         print(middlevalue,end="")

    #rightnumber
    number=i
    if number != mid:
        print(number,end="")

    print()
    i=i+1
#lowerhalf
i=mid-1
while i >= 1:
    j=1
    #leftspace
    while j <=i-1:
        print(" ",end="")
        j=j+1
    #leftnumber
    print(i,end="")

    #middlespace
    middlespace=1
    while middlespace <= 2*(mid-i):
        print(" ",end="")
        middlespace=middlespace+1

    #rightnumber
    number=i
    if number != mid:
        print(number,end="")

    print()
    i=i-1