n = int(input("Enter number: "))

a = 0
b = 1

while True:

    if a > n:
        print("NO")
        break

    if a == n:
        print("YES")
        break

    temp = a + b
    a = b
    b = temp