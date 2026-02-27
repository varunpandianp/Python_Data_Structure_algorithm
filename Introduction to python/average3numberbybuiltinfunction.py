# Take input from user
numbers = input("Enter numbers separated by space: ")

# Convert string input into list of integers
num_list = list(map(float, numbers.split()))

# Check if list is not empty
if len(num_list) > 0:
    average = sum(num_list) / len(num_list)
    print("Average:", average)
else:
    print("No numbers entered!")