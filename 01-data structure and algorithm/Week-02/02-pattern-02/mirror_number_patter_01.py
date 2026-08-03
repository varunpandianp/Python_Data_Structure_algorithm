# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
#
#

n = int(input("enter the value :"))

i = 1

while i <=n:
    space = 1

    while space <= n-i:
        print(" ",end="")
        space = space+1
    star = 1
    while star <= i :
        print(star,end="")
        star=star+1
    print()
    i=i+1