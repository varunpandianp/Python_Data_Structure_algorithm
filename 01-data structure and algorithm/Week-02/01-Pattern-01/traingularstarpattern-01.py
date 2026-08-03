# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# *
# **
# ***
# ****
# Note : There are no spaces between the stars (*).

n = int(input("enter the value: "))
i = 1
while i <=n :
    j = 1
    p = i
    while j <= p:
        print("*",end="")
        j=j+1
    print()
    i = i+1
