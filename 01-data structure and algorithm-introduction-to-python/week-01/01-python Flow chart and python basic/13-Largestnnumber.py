# find largest of n number for that we need to how mny number to get from the user
#for that we need the range how many number input
#from that we need to check each number each other to find the largest number

#get the range of number to from the user

n = int(input("enter the how many number to find the Largest no"))

#input given for the largest number to check on the first loop

largest = -99999

for i in range(n):
    num = int(input("enter the number"))
    if num>n:
          largest = num
print("largest num is",largest)

