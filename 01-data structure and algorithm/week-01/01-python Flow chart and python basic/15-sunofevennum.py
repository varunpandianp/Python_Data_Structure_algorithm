n = int(input("enter the positive integer"))

sum=0
i =1

while i <= n:
    if i%2==0:
        sum=sum+i
    i = i+1

print("sum of even number",sum)