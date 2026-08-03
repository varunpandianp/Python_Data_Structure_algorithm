# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# 4444
# 333
# 22
# 1

n = int(input("enter the value: "))

i = 1

while i <= n:
    j=1
    print_value= n-i+1
    while j <= n-i+1:
        print(print_value,end="")
        j = j+1
    print()
    i = i+1