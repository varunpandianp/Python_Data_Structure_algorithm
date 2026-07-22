# Print the following pattern for the given number of rows.
#
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input("enter the value"))

i = 1
while i <= n:
    j = 0
    start_value=chr(ord('A') +n -i)
    while j < i:
        character=chr(ord(start_value)+j )
        print(character,end="")

        j=j+1
    print()
    i = i+1