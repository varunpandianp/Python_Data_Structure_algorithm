# You are given first three entries of an arithmetic progression. \
# You have to calculate the common difference and print it.

E1 = int(input("Enter the first no"))
E2 = int(input("Enter the second no"))
E3 = int(input("Enter the third no"))


if E2-E1 == E3-E2:
    output=E3-E2
    print("Result Arithmetic progression",output)
else:
    print("Not an arithmetic progression")




