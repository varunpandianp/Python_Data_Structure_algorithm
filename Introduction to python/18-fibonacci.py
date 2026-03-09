n = int(input("Enter number: "))

a = 0
b = 1

while b < n:
    c = a + b
    a = b
    b = c

if n == 0 or b == n:
    print("Yes")
else:
    print("No")