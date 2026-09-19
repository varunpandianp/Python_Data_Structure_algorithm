# You are given a single positive integer, N. You need to find and print whether N is Prime or not.
#
# Draw a flowchart for this process
#
# Note: You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.

n = int(input("enter num to find prime no or not"))

#  prime = 2

if n <= 1 :
     print("its not prime number")
else:
     for i in range(2 ,n):
         if n%i == 0:
             print("given number is not prime")
             break
     else:
         print("Given number is prime")