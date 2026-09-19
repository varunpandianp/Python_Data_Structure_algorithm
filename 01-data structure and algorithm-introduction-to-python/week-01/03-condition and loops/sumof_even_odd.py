# Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.
#
#
#
# Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits are 1, 3, and 5.
#
# Constraints
# 0<= 'n' <=10000
#
#
# Example :
# Input: 'n' = 132456
#
# Output: 12 9
#
# Explanation:
# The sum of even digits = 2 + 4 + 6 = 12
# The sum of odd digits = 1 + 3 + 5 = 9
# Constraints
# 0<= 'n' <=10000

n = int(input("enter the value : "))

sum_of_even=0
sum_of_odd=0

while n != 0:
    digits = n % 10
    if(digits % 2 == 0):
        sum_of_even = sum_of_even + digits
    else:
        sum_of_odd = sum_of_odd+digits
    n = n//10
value = f"the sum of even {sum_of_even} and sum of odd value {sum_of_odd}"
print(value)