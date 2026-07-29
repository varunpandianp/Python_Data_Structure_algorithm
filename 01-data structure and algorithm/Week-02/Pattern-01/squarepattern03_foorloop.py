n = int(input("Enter the value: "))

for i in range(n):
    for j in range(n, 0, -1):
        print(j, end="")
    print()