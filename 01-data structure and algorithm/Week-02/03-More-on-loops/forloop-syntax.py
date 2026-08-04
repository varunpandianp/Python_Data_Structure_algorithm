s = "abcd"
for c in s:
    print(c)

1. Using range()
Print 1 to 5
for i in range(1, 6):
    print(i)

Print 0 to 4
for i in range(5):
    print(i)

2. Loop through a list
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

3. Loop through a string
name = "Python"

for letter in name:
    print(letter)

4. Using step in range()
Print even numbers
for i in range(2, 11, 2):
    print(i)

Print in reverse
for i in range(10, 0, -1):
    print(i)

5. Sum of numbers
total = 0

for i in range(1, 6):
    total = total + i

print(total)

6. Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

7. Multiplication Table
num = 5

for i in range(1, 11):
    print(num, "*", i, "=", num * i)

8. Pattern
for i in range(1, 6):
    print("*" * i)

Understanding range()
Code	Meaning
range(5)	0, 1, 2, 3, 4
range(1, 6)	1, 2, 3, 4, 5
range(2, 11, 2)	2, 4, 6, 8, 10
range(10, 0, -1)	10, 9, ..., 1