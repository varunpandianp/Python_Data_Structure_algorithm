# Write a prgram that perfrms the tasks f a simple calculatr. The prgram shuld first take an integer as input and then based n that integer perfrm the task as given belw. Yu shuld als take an integer n that wuld actually tell us hw many times will the peratins be perfrmed.
#
# 1. If the input is 1, then 2 integers are taken frm the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken frm the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken frm the user and their prduct is printed.
# 4. If the input is 4, then 2 integers are taken frm the user and the qutient btained (n dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken frm the user and their remainder(1st number md 2nd number) is printed.
# 6. If the input is 6, then the prgram exits.
# 7. Fr any ther input, then print "Invalid peratin".
# Nte: Each answer in next line.

o = int(input("enter the number:"))

while  o != 6:
    if  o <= 5 and o >= 1:
        a = int(input("enter the number:"))
        b = int(input("enter the number:"))

    elif  o == 1:
        print(a+b)
    elif o == 2:
        print(a-b)
    elif o ==3:
        print(a*b)
    elif o == 5:
        print(a//b)

    o= int(input("enter the value"))
else:
     print("invalid operation")