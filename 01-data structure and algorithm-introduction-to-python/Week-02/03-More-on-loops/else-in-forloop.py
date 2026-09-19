numbers = [2, 4, 6, 8]

for num in numbers:
    if num == 5:
        print("Found")
        break
else:
    print("Not Found")

#Without else

   flag = False

    for d in range(2, n):
        if n % d == 0:
            flag = True
            break

    if flag:
        print("Not Prime")
    else:
        print("Prime")

#With for  Else

for d in range(2, n):
    if n % d == 0:
        print("Not Prime")
        break
else:
    print("Prime")