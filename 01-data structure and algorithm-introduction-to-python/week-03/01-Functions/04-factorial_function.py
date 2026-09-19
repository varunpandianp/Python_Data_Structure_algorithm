n = int(input(""))
r = int(input(""))

def factorial(num):
    fact = 1

    for i in range(1,num+1):
        fact = fact*i

    return fact

n_fact=factorial(n)
r_fact=factorial(r)
n_r_fact=factorial(n-r)
ans = n_fact//(r_fact*n_r_fact)
print(ans)