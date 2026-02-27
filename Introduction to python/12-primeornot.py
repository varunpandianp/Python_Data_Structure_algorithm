n = int(input("Enter the number to find prime or not"))

if n <= 1:
    print("its not prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Not prime number")
            break
        i = i + 1
    else:
        print("given number prime")