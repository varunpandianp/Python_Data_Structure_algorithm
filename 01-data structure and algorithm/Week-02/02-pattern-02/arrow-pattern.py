# Problem statement
# Print the following pattern for the given number of rows.
#
# Assume N is always odd.
#
# Note : There is space after every star. Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

N=int(input())
i=1
mid=N//2+1
while i <=mid:
    #space print
    space = 1
    while space <= 2 * (i - 1):
        print(" ",end="")
        space=space+1
    #left side
    star=1
    while star<=i:
        print("* ",end="")
        star=star+1
    print()
    i=i+1

i = mid - 1
while i >= 1:
    #space print
    space = 1
    while space <= 2 * (i - 1):
        print(" ",end="")
        space=space+1
#left side
    star=1
    while star<=i:
        print("* ",end="")
        star=star+1
    print()
    i=i-1



