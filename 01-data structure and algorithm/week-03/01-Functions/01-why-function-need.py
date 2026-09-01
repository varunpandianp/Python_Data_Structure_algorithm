# n = int(input(""))
# r = int(input(""))
#
# n_fact = 1
# for i in range(1,n+1):
#     n_fact=n_fact*i
#
# r_fact = 1
# for i in range(1,r+1):
#     r_fact=r_fact*i
#
# n_r_fact= 1
# for i in range(1,n-r+1):
#     n_r_fact=n_r_fact*i
#
# ans = n_fact//(r_fact*n_r_fact)
#
# print(ans)


n = int(input())
r = int(input())

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


n_fact = factorial(n)
r_fact = factorial(r)
n_r_fact = factorial(n - r)

ans = n_fact // (r_fact * n_r_fact)

print(ans)

