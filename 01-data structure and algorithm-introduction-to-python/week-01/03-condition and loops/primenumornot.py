n = int(input("enther the value : "))

d = 2
is_prime = True

while d < n:
    if n % d == 0:
        is_prime  = False
        print("num", n, "divisible by", d, "=", n%d)
        break
    d = d+1

if is_prime:
    print("given Number is prime")
else:
    print("Given number is not prime")