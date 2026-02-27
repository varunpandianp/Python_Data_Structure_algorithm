# You are given a single positive integer, N. You need to print all even integers that occur between 1 and N (both inclusive).
#
# Draw a flowchart for this process
#
# Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.

n = int(input("enter the N no to find the interger"))



if n > 0:
    even = 2
    for i in range(1,1+n):
        if i%even == 0:
            print(i,end=(","))
        else:
            print(end=(" "))

else:
    print("enter the positive number")



