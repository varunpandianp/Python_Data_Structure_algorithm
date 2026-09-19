# Problem statement
# Given an integer n, find and print the sum of numbers from 1 to n.
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= n <= 100
#
# Sample Input :
# 10
# Sample Output :
#55

n = int(input("Enter the value"))
sumofnumber = 0

if n >= 1 and n <= 100:
    number=1
    while number <= n:
        sumofnumber=sumofnumber+number
        number = number+1
    print(sumofnumber)

else:
    print("enter number between 1 to 100")