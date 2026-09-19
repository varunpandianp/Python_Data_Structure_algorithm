n = int(input("enter the value to check palindrome:"))

manipulate_number_intialvalue=0
remaining_Value = n

while remaining_Value != 0:
    digit = remaining_Value % 10
    manipulate_number_intialvalue=manipulate_number_intialvalue*10+digit
    remaining_Value=remaining_Value//10

if(n == manipulate_number_intialvalue):
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")