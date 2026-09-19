Functions in Python
A function is a reusable block of code that performs a specific task.
Instead of writing the same code repeatedly, we write it once inside a function and call it whenever needed.
1. Basic syntax
   def function_name():
   # code

Example:
def greet():
print("Hello")

greet()

Output:
Hello
Here:
- def → keyword used to define a function
- greet → function name
- () → parameters go here
- : → starts the function body
- greet() → function call

2. Function with parameters
   Parameters allow us to pass data into a function.
   def greet(name):
   print("Hello", name)

greet("Varun")
greet("Rahul")

Output:
Hello Varun
Hello Rahul
Think of it as:
greet("Varun")
↓
name = "Varun"
3. Function with multiple parameters
   def add(a, b):
   print(a + b)

add(10, 20)

Output:
30
Here:
a = 10
b = 20
4. return — very important
   return sends a value back to the place where the function was called.
   def add(a, b):
   return a + b

result = add(10, 20)

print(result)

Output:
30
Think:
add(10, 20)
↓
10 + 20
↓
return 30
↓
result = 30
Important difference
def add(a, b):
print(a + b)

This prints the result.
Whereas:
def add(a, b):
return a + b

This returns the result so you can store/use it.

6. Function with default parameter
   def greet(name="Varun"):
   print("Hello", name)

greet()
greet("Rahul")

Output:
Hello Varun
Hello Rahul
If you don't provide an argument, the default value is used.
7. Function returning multiple values
   Python can return multiple values:
   def calculate(a, b):
   return a + b, a - b

x, y = calculate(10, 5)

print(x)
print(y)

Output:
15
5
8. Function with if
   def check_even(n):
   if n % 2 == 0:
   return True
   else:
   return False

print(check_even(10))

Output:
True
You can simplify it:
def check_even(n):
return n % 2 == 0

9. Function with for loop — important for DSA
   Example: prime number checking.
   def is_prime(n):

   if n < 2:
   return False

   for i in range(2, n):

        if n % i == 0:
            return False

   return True

print(is_prime(7))
print(is_prime(10))

Output:
True
False
How it works for 10
i = 2
10 % 2 == 0
↓
return False
The function immediately stops.
That's why:
return False

inside the loop is useful.
You don't need break in this case because return itself exits the entire function.
10. break vs return
    This is particularly important for your DSA practice.
    break
    Stops the loop:
    for i in range(10):

    if i == 5:
    break

print("Function continues")

The function can continue after the loop.
return
Stops the entire function:
def test():

    for i in range(10):

        if i == 5:
            return False

    return True

When i == 5:
return False
↓
loop stops
↓
function stops
The final:
return True

is never executed.

Function execution flow
Remember this structure:
Define function
↓
Call function
↓
Arguments → Parameters
↓
Execute function body
↓
return value
↓
Use returned value
Example:
def square(n):
return n * n

result = square(5)

print(result)

Flow:
square(5)
↓
n = 5
↓
5 * 5
↓
return 25
↓
result = 25
↓
print(result)
Core things you should master now
For Python/DSA, focus on these in order:
1. def
2. Function call
3. Parameters and arguments
4. return
5. Local vs global variables
6. Default arguments
7. Multiple parameters
8. Functions with if/else
9. Functions with for/while
10. Functions calling other functions
11. Recursion
12. *args and **kwargs
    Most important concept for you right now: understand exactly how parameters → function execution → return → variable assignment works. This will make your upcoming DSA problems much easier.
    Function execution flow
    Remember this structure:
    Define function
    ↓
    Call function
    ↓
    Arguments → Parameters
    ↓
    Execute function body
    ↓
    return value
    ↓
    Use returned value
    Example:
    def square(n):
    return n * n

result = square(5)

print(result)

Flow:
square(5)
↓
n = 5
↓
5 * 5
↓
return 25
↓
result = 25
↓
print(result)
Core things you should master now
For Python/DSA, focus on these in order:
1. def
2. Function call
3. Parameters and arguments
4. return
5. Local vs global variables
6. Default arguments
7. Multiple parameters
8. Functions with if/else
9. Functions with for/while
10. Functions calling other functions
11. Recursion
12. *args and **kwargs
    Most important concept for you right now: understand exactly how parameters → function execution → return → variable assignment works. This will make your upcoming DSA problems much easier.