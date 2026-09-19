n= int(input("enter the fibonnaic value num you want :" ))

if n == 1 :
    print("Fibonnaci num is 1")
if n == 2:
    print("Fibonnaci num is 1")

first_number = 1


second_number = 1

count = 2

while count < n :
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
    count = count + 1
print(next_number)

