n = int(input("Enter number: "))

a = 0
b = 1

while b <= n:
    print(b,end=" ")

    c = a + b
    a = b
    b = c