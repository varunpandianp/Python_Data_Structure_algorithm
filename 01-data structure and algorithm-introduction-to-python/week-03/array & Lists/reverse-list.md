# **REVERSE IN LIST**

## **1. What is Reverse?**

Reversing a list means changing the order of elements from last to first.

Example:

```python
numbers = [10, 20, 30, 40, 50]

After reversing:
[50, 40, 30, 20, 10]
```
## 2. Using reverse()
   Python provides the reverse() method to reverse a list.
   Example:
   numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)

Output:
[50, 40, 30, 20, 10]

## 3. Important Point About reverse()
   reverse() changes the original list.
   Example:
   numbers = [10, 20, 30]

numbers.reverse()

print(numbers)

Output:
[30, 20, 10]
The original list itself is changed.

## 4. Reverse Using Slicing
   We can also reverse a list using:
   numbers = [10, 20, 30, 40, 50]

result = numbers[::-1]

print(result)

[::-1] means:
Start from the end
Move backwards
Step = -1

## 5. reverse() vs [::-1]
   reverse():
   numbers.reverse()

- Changes the original list.
- Does not create a new reversed list.
  [::-1]:
  result = numbers[::-1]

- Creates a new reversed list.
- Original list remains unchanged.

## 7. Reverse Using a Loop
   We can also reverse a list manually using a loop.
   numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) - 1, -1, -1):
print(numbers[i])

Here:
range(len(numbers) - 1, -1, -1)

means:
Start → last index
Stop  → before -1
Step  → -1

# **REVERSE A LIST USING SWAPPING**

## **1. What is Swapping?**

Swapping means exchanging the values of two variables.

Example:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)

```

## 2. Reverse a List Using Swapping
   Example:
   numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) // 2):
numbers[i], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[i]

print(numbers)

Output:
[50, 40, 30, 20, 10]
## 3. How Does It Work?
   List:
   Index:    0    1    2    3    4
   Value:   10   20   30   40   50
   We swap:
   10 ↔ 50
   20 ↔ 40
   The middle element 30 does not need to be swapped.
## 4. Why len(numbers) // 2?
   Suppose:
   numbers = [10, 20, 30, 40, 50]

Length:
len(numbers) = 5

Then:
len(numbers) // 2

gives:
5 // 2 = 2
So:
range(2)

gives:
0, 1
Only two swaps are needed:
Index 0 ↔ Index 4
Index 1 ↔ Index 3
The middle element is already in the correct position.
## 5. Why Use // Instead of /?
   / gives a float:
   5 / 2

Output:
2.5
// gives the floor integer:
5 // 2

Output:
2
We need an integer for range().
## 6. Understanding the Formula
   numbers[len(numbers) - 1 - i]

This gives the element from the opposite end.
For:
numbers = [10, 20, 30, 40, 50]
When i = 0:
len(numbers) - 1 - i
5 - 1 - 0
= 4
So:
numbers[0] ↔ numbers[4]

10 ↔ 50
When i = 1:
5 - 1 - 1
= 3
So:
numbers[1] ↔ numbers[3]

20 ↔ 40
## 7. Easy Version to Remember
   numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) // 2):
numbers[i], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[i]

print(numbers)

Think:
First ↔ Last
Second ↔ Second Last
Continue until the middle
## 8. Important Concept
   a, b = b, a

means:
Swap a and b
And:
range(len(numbers) // 2)

means:
Loop only through half of the list