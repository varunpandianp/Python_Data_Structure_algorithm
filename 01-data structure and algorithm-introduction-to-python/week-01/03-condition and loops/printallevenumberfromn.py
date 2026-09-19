n = int(input("enter the value :"))

divisiblevalue = 2
d=2
while d <= n:
    if d % divisiblevalue == 0:
        print("Prime Number is",d,)
    d=d+1
