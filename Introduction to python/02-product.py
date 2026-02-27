# You are given a single non-negative integer, N. You need to calculate and print N factorial (N!)
#
# N factorial is defined as the product of all integers from 1 to N (both inclusive)
#
# Draw a flowchart for this process
#
# Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.

n = int(input("enter the factorial N value no"))



if n > 0:
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i

        if i != 1 :
            print(i, end=" * ")
        else:
            print(i, end="  ")
    print("factorial of the given N no is",fact)



else:

    print("enter the value above 0")
