# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
#
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

n = int(input("enter the number to reverse"))
reverse_number =0
while n > 0:
    reverse_digit=n%10
    reverse_number=reverse_number*10+reverse_digit
    n = n//10
print(reverse_number)

# 1. Digit Manipulation ⭐⭐⭐⭐⭐ (Most common name)
#
# This entire problem belongs to the Digit Manipulation category.
#
# Examples include:
#
# Reverse a number
# Palindrome number
# Sum of digits
# Count digits
# Armstrong number
# Strong number
# Harshad number