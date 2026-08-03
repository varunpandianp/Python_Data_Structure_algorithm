# Problem statement
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# A
# BC
# CDE
# DEFG

n = int(input("enter the value"))

i = 1

while i <=n :

    j = 1
    start_value = chr(ord('A') +i -1)

    while j <= i:
        character = chr(ord(start_value) +j -1)
        print(character,end="")
        j = j+1
    print()
    i = i+1