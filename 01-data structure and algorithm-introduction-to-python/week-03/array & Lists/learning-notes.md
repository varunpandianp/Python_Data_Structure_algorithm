# PYTHON LISTS

## 1. What is a List?

A **list** is used to store multiple values in a single variable.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

Instead of creating separate variables:

```python
a = 10
b = 20
c = 30
d = 40
e = 50
```

We can store all values in one list:

```python
numbers = [10, 20, 30, 40, 50]
```

---

# 2. Accessing List Elements Using Index

Python uses **index numbers** to access elements.

Important:

**Python indexing starts from 0.**

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[2])
```

Output:

```text
10
20
30
```

Index structure:

```text
Value:   10    20    30    40    50
Index:    0     1     2     3     4
```

For example:

```python
numbers[0]    # 10
numbers[2]    # 30
numbers[4]    # 50
```

---

# 3. List Can Contain Different Data Types

Python lists are flexible.

A list can contain:

- Integers
- Strings
- Floats
- Booleans
- Other lists

Example:

```python
data = [10, "hello", 3.5, True]

print(data)
```

Another example:

```python
student = ["Varun", 33, "DevOps"]
```

---

# 4. List vs Array

In many programming languages, an **array** usually stores values of the same data type.

Example in Java:

```java
int[] numbers = {10, 20, 30, 40};
```

In Python, we commonly use a **list**:

```python
numbers = [10, 20, 30, 40]
```

So when solving Python DSA problems, you will frequently work with **lists**.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

Even if a DSA question says **array**, the Python solution will commonly use a list.

---

# 5. List is Mutable

**Mutable** means we can change the list after creating it.

Example:

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

We changed:

```text
10 → 100
```

---

# 6. Adding Elements to a List

## 6.1 append()

`append()` adds an element to the **end of the list**.

Syntax:

```python
list.append(value)
```

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Remember:

```text
append() → adds at the end
```

---

## 6.2 insert()

`insert()` adds an element at a **specific index**.

Syntax:

```python
list.insert(index, value)
```

Example:

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

Output:

```text
[10, 15, 20, 30]
```

Here:

```python
numbers.insert(1, 15)
```

means:

```text
Index 1 → insert 15
```

Remember:

```text
insert() → adds at a specific index
```

---

# 7. Removing Elements from a List

There are two important methods:

```text
remove()
pop()
```

The main difference:

```text
remove() → removes by VALUE
pop()    → removes by INDEX
```

---

## 7.1 remove()

`remove()` removes a specific **value** from the list.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)
```

Output:

```text
[10, 20, 40]
```

Here:

```python
numbers.remove(30)
```

means:

```text
Find the value 30 → remove it
```

Important:

```python
numbers.remove(2)
```

means:

```text
Remove VALUE 2
```

It does NOT mean:

```text
Remove INDEX 2
```

---

## 7.2 pop()

`pop()` removes an element using its **index**.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.pop(2)

print(numbers)
```

Output:

```text
[10, 20, 40]
```

Index structure:

```text
Value:   10    20    30    40
Index:    0     1     2     3
                     ↑
                   pop(2)
```

So:

```python
numbers.pop(2)
```

means:

```text
Remove the element at INDEX 2
```

---

## 7.3 pop() Without an Index

If we don't provide an index, `pop()` removes the **last element**.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
```

Output:

```text
[10, 20, 30]
```

So:

```text
pop() → removes last element
pop(index) → removes element at that index
```

---

## 7.4 remove() vs pop()

```text
remove() → VALUE
pop()    → INDEX
```

Example:

```python
numbers = [10, 20, 30, 40]

numbers.remove(30)    # Removes VALUE 30
```

Whereas:

```python
numbers = [10, 20, 30, 40]

numbers.pop(2)        # Removes INDEX 2
```

Both remove `30`, but they work differently.

---

## 7.5 pop() Can Return the Removed Value

`pop()` returns the element that it removed.

Example:

```python
numbers = [10, 20, 30, 40]

x = numbers.pop(2)

print(x)
print(numbers)
```

Output:

```text
30
[10, 20, 40]
```

So:

```python
x = numbers.pop(2)
```

does two things:

1. Removes `30`
2. Returns `30`

---

# 8. List Slicing

**Slicing** means taking a portion of a list.

Basic syntax:

```python
list[start : stop]
```

Important:

```text
START → included
STOP  → NOT included
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Index:

```text
Value:   10    20    30    40    50
Index:    0     1     2     3     4
                ↑           ↑
              START        STOP
```

`1:4` means:

```text
Start at index 1
Stop before index 4
```

Therefore:

```text
20, 30, 40
```

---

# 9. Common Slicing Examples

## Start from a specific index

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

Output:

```text
[30, 40, 50]
```

Meaning:

```text
Start from index 2 and go until the end.
```

---

## Start from the beginning

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

Output:

```text
[10, 20, 30]
```

Meaning:

```text
Start from the beginning and stop before index 3.
```

---

## Copy the entire list

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:])
```

Output:

```text
[10, 20, 30, 40, 50]
```

`[:]` means the entire list.

---

# 10. Slicing with Step

Syntax:

```python
list[start : stop : step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])
```

Output:

```text
[10, 30, 50]
```

Here:

```text
start = 0
stop  = 6
step  = 2
```

It takes every 2nd element.

---

## Step = 1

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:5:1])
```

Output:

```text
[10, 20, 30, 40, 50]
```

Step `1` means:

```text
Take every element.
```

---

## Step = 2

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:5:2])
```

Output:

```text
[10, 30, 50]
```

---

# 11. Negative Indexing

Python also supports negative indexes.

```text
Value:      10    20    30    40    50
Positive:    0     1     2     3     4
Negative:   -5    -4    -3    -2    -1
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
```

Output:

```text
50
```

Remember:

```text
-1 → last element
-2 → second-last element
-3 → third-last element
```

---

# 12. Reverse a List Using Slicing

We can use a negative step to move backwards.

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

Remember:

```python
[::-1]
```

means:

```text
Start from the end
Move backwards
Step = 1
```

It is a common Python technique for reversing a list.

---

# 13. Important Slicing Examples

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]
[10, 20, 30, 40, 50]
[10, 30, 50]
[50, 40, 30, 20, 10]
```

---

# 14. Loop Through a List

Looping through a list is very important for DSA.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
```

Output:

```text
10
20
30
40
50
```

Here:

```python
for num in numbers:
```

means:

```text
Take each element from numbers one by one
and store it temporarily in num.
```

---

# 15. Loop Through a List Using Index

We can also access elements using their index.

```python
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(numbers[i])
```

Output:

```text
10
20
30
40
50
```

Here:

```python
len(numbers)
```

gives the number of elements.

For example:

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

Output:

```text
5
```

---

# 16. Important List Methods

```text
append()  → Add element at the end
insert()  → Add element at a specific index
remove()  → Remove by value
pop()     → Remove by index
pop()      → Remove last element
len()     → Find number of elements
```

Example:

```python
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(30)
numbers.pop(0)

print(numbers)
```

---

# 17. Quick Revision

## List

```python
numbers = [10, 20, 30, 40, 50]
```

## Indexing

```python
numbers[0]
numbers[1]
numbers[-1]
```

## Changing Values

```python
numbers[0] = 100
```

## Adding

```python
numbers.append(60)
numbers.insert(1, 15)
```

## Removing

```python
numbers.remove(30)   # By VALUE
numbers.pop(2)       # By INDEX
numbers.pop()        # Last element
```

## Length

```python
len(numbers)
```

## Slicing

```python
numbers[start:stop]
numbers[start:stop:step]
```

## Reverse

```python
numbers[::-1]
```

## Loop

```python
for num in numbers:
    print(num)
```

---

# 18. Most Important Rule for Slicing

Always remember:

```text
[START : STOP : STEP]
```

```text
START → Where to begin
STOP  → Where to stop (NOT included)
STEP  → How many positions to move
```

Examples:

```text
numbers[1:4]      → index 1 to 3
numbers[:3]       → beginning to index 2
numbers[2:]       → index 2 to end
numbers[:]        → entire list
numbers[::2]      → every 2nd element
numbers[::-1]     → reverse the list
```

---

# Python List Learning Order

```text
List
  ↓
Indexing
  ↓
Negative Indexing
  ↓
Changing Elements
  ↓
append()
  ↓
insert()
  ↓
remove()
  ↓
pop()
  ↓
len()
  ↓
Slicing
  ↓
Slicing with Step
  ↓
Reverse using [::-1]
  ↓
for Loop with List
  ↓
List + Functions
  ↓
List DSA Problems
```

## Key Things to Remember

```text
List              → Stores multiple values
Index              → Starts from 0
Mutable             → List values can be changed
append()            → Add at end
insert()            → Add at specific index
remove()            → Remove by VALUE
pop()               → Remove by INDEX
pop()               → Without index removes last element
len()               → Number of elements
Slicing             → Get a portion of a list
[start:stop:step]   → Slicing format
[::-1]              → Reverse a list
```

# LINE-SEPARATED vs SPACE-SEPARATED INPUT

## 1. Line-Separated Input

Each value is given on a separate line.

Input:
```text
10
20
30
40
50
```

Python:
```python
for i in range(5):
    num = int(input())
    print(num)
```

---

## 2. Space-Separated Input

All values are given on the same line, separated by spaces.

Input:
```text
10 20 30 40 50
```

Python:
```python
numbers = list(map(int, input().split()))
```

Output:
```text
[10, 20, 30, 40, 50]
```

---

## How input().split() works

```python
input().split()
```

Input:
```text
10 20 30 40 50
```

After `split()`:
```text
["10", "20", "30", "40", "50"]
```

`map(int, ...)` converts strings to integers.

`list(...)` converts them into a list.

Final:
```text
[10, 20, 30, 40, 50]
```

---

## QUICK REMEMBER

```text
Line-separated:
10
20
30

Space-separated:
10 20 30
```

For space-separated numbers, commonly use:

```python
numbers = list(map(int, input().split()))
```

split() → separates values by spaces
map(int) → converts strings to integers
list() → creates a list

LINEAR SEARCH IN LIST
=====================

1. WHAT IS LINEAR SEARCH?

Linear Search means checking each element in a list one by one until the target element is found or the list ends.


2. BASIC EXAMPLE

numbers = [10, 20, 30, 40, 50]

target = 30

for ele in numbers:
if ele == target:
print("Found")
break


OUTPUT:

Found


3. HOW IT WORKS

List:
[10, 20, 30, 40, 50]

Target:
30

Checking:

10 == 30  -> No
20 == 30  -> No
30 == 30  -> Yes -> Found


4. LINEAR SEARCH WITH INDEX

numbers = [10, 20, 30, 40, 50]

target = 30

for i in range(len(numbers)):
if numbers[i] == target:
print("Found at index", i)
break


OUTPUT:

Found at index 2


5. IF ELEMENT IS NOT FOUND

numbers = [10, 20, 30, 40, 50]

target = 60
found = False

for ele in numbers:
if ele == target:
found = True
break

if found:
print("Found")
else:
print("Not Found")


OUTPUT:

Not Found


6. TIME COMPLEXITY

Best Case  -> O(1) -> Target is the first element

Worst Case -> O(n) -> Target is the last element or not present


7. REMEMBER

Linear Search = Check elements one by one.

for ele in list:
if ele == target:
Found


8. EASY DEFINITION

Linear Search is a searching technique where each element of a list is checked one by one until the target is found or the list ends.

# **MUTABLE AND IMMUTABLE IN PYTHON**

## **1. WHAT IS MUTABLE?**

Mutable means an object can be changed after it is created.

Example:

python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers) 
 

## 2. WHAT IS IMMUTABLE?
Immutable means an object cannot be changed after it is created.
Example:
name = "Varun"

name[0] = "X"

This gives an error because strings are immutable.
We cannot directly change a character inside an existing string.
## 3. LIST IS MUTABLE
A list can be changed after creation.
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

Output:
[10, 20, 30, 40]
We can:
numbers[0] = 100
numbers.append(40)
numbers.pop()

These operations modify the list.
## 4. TUPLE IS IMMUTABLE
Example:
numbers = (10, 20, 30)

numbers[0] = 100

This gives an error.
We cannot change an element inside an existing tuple.
## 5. COMMON MUTABLE TYPES
- List
- Dictionary
- Set
## 6. COMMON IMMUTABLE TYPES
- Integer
- Float
- String
- Boolean
- Tuple
## 7. MUTABLE VS IMMUTABLE
Mutable:
Can be changed after creation.
Immutable:
Cannot be changed after creation.

# **PASSING VARIABLES THROUGH A FUNCTION**

## **1. What Does Passing a Variable Mean?**

Passing a variable means sending a value to a function as an argument.

The function receives that value through a parameter.

## **2. Simple Example**

```python
def add(num):
    print(num + 10)

x = 5

add(x)

5. Easy Definition
Passing a variable through a function means passing the value/reference of a variable to a function as an argument so the function can use it.
Remember
Variable outside function → Argument
Variable inside function  → Parameter

Example:

x = 10

func(x)
     ↑
   argument

def func(a):
         ↑
      parameter

