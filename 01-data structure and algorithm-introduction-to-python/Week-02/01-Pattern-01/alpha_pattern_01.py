# 3)Problem statement
# Print the following pattern for the given N number of rows.
# Pattern for N = 3
# A
#  BB
#  CCC

n = int(input("Enter the value:"))
i = 0

while i <= n:
    j = 0
    star_char=chr(ord('A')+i)

    while (j<=i):
        print ( star_char,end="")
        j = j+1

    print()

    i = i+1