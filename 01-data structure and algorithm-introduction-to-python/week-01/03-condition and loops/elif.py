a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_value = a + b          # Arithmetic operator

is_positive = (a > 0 and b > 0)   # Relational + Logical -> Boolean

if is_positive and sum_value > 100:
    print("Both positive and sum greater than 100")

elif is_positive and sum_value >= 50:
    print("Both positive and sum between 50 and 100")

elif is_positive:
    print("Both positive but sum less than 50")

else:
    print("One or both numbers are not positive")