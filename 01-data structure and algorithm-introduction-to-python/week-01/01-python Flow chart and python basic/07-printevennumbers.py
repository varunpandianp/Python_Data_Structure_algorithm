n = int(input("Enter N: "))

if n > 0:
    evens = []
    for i in range(2, n+1, 2):
        evens.append(str(i))
    print(", ".join(evens))
else:
    print("Enter positive number")