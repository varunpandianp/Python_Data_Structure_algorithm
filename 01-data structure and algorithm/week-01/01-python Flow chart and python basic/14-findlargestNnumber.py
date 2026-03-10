n = int(input("type N range "))
i = 1
l = -10000000

while i <= n:
    num = int(input("enter the number"))
    if num > l:
        l = num
    i=i+1

print("Largest Num",l)

