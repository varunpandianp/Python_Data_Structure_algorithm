# Problem statement
# Given a number N, print sum of all even numbers from 1 to N.
#
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
#  6
# Sample Output 1 :
# 12
# Sample Input 2 :
#  7
# Sample Output 2 :
# 12

n = int(input("enter the value for sum of even number"))

sumofeven = 0

currentvalue = 1

while currentvalue <= n:
    if currentvalue % 2 ==0 :
        #print(currentvalue)
        sumofeven = currentvalue + sumofeven
    currentvalue = currentvalue + 1


print(sumofeven)
