def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True

    return False

n=int(input())


def print_prime_from_TO_N(n):
    for k in range(2,n+1):
        is_k_prime = isprime (k)
        if (is_k_prime):
            print(k)

print(print_prime_from_TO_N(n))