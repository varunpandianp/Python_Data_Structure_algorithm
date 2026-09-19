n = int(input("enter the value : "))

d = 2

while d <= n:
    divisor = 2
    is_prime = True

    while divisor < d:
        if d % divisor == 0:
            is_prime = False
            break
        divisor = divisor + 1

    if is_prime:
        print(d)
    d = d + 1
