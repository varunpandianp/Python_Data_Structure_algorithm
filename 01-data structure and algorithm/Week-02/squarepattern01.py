#pattern problem to learn how nested loop work
# Print the following pattern for the given N number of rows.
#
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444

n = int(input("Enter the no "))

i = 1

while i <= n:
    j=1

    while j <= n:
        print(n,end=" ")
        j =j+1
    print()
    i = i+1