date:19-09-2026 

## Scope of Variables in Python
Scope means:
Where a variable can be accessed/used in a program.

The most important thing to understand with functions is local scope vs global scope.
## 1. Local Variable
   A variable created inside a function is called a local variable.
   def test():
   x = 10
   print(x)

test()

Output:
10
But this won't work:
def test():
x = 10

test()

print(x)

You get an error because x exists only inside test().
Outside function
❌ x not available

      ↓

def test():
x = 10
↑
available here
Remember
Local variable = accessible only inside its function.

## 2. Global Variable
   A variable created outside all functions is a global variable.
   x = 10

def test():
print(x)

test()

Output:
10
The function can read the global variable.
x = 10        ← Global
↓
test()
↓
print(x)      ← Can access it
3. Local and Global with Same Name
   This is very important.
   x = 10

def test():
x = 20
print(x)

test()

print(x)

Output:
20
10
Why?
There are actually two different x variables.
Global:
x = 10

Function:
x = 20
Inside the function, Python uses the local x.
Outside the function, Python uses the global x.
4. Function Cannot Normally Modify Global Variable
   Example:
   x = 10

def test():
x = 20

test()

print(x)

Output:
10
The x = 20 creates a new local variable.
It doesn't change the global x.
5. global Keyword
   If you really want to modify the global variable from inside a function, use global.
   x = 10

def test():
global x
x = 20

test()

print(x)

Output:
20
Now Python knows:
global x

means:
"Use the global x, not a new local x."

6. Function Parameters Are Local Variables
   This is extremely important for your DSA practice.
   def add(a, b):
   result = a + b
   return result

print(add(10, 20))

Inside the function:
a       → local
b       → local
result  → local
They belong to that particular function call.
After the function returns, those local variables are no longer accessible from outside.
7. Scope + Function Call
   Look at this:
   x = 5

def test(x):
x = x + 10
return x

print(test(x))
print(x)


8. LEGB Rule
   Python decides which variable to use using the LEGB rule.
   L → Local
   E → Enclosing
   G → Global
   B → Built-in
   L — Local
   Inside the current function:
   def test():
   x = 10

E — Enclosing
Used with nested functions:
def outer():
x = 10

    def inner():
        print(x)

inner() can access x from outer().
G — Global
Outside functions:
x = 10

def test():
print(x)

B — Built-in
Python's built-in names:
print()
len()
sum()
range()
int()

Simple LEGB Example
x = "global"

def outer():
x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()

Output:
local
Python searches:
Local
↓
Enclosing
↓
Global
↓
Built-in
It uses the first matching variable it finds.

⭐ Notes to Remember
SCOPE OF VARIABLES
------------------

Local:
Created inside a function.
Accessible inside that function.

Global:
Created outside functions.
Can be read inside functions.

Parameter:
A parameter is local to the function.

global keyword:
Used when a function needs to modify a global variable.

LEGB:
Local → Enclosing → Global → Built-in

# Default Parameters in Python Functions

## What is a Default Parameter?

A **default parameter** is a parameter that already has a value.

If we don't pass a value while calling the function, Python uses the **default value**.

## Syntax

```python
def function_name(parameter=default_value):
    # code
```

## Example

```python
def greet(name="Varun"):
    print("Hello", name)

greet()
```

Output:

```text
Hello Varun
```

Here:

```python
name="Varun"
```

is the **default parameter**.

Since we called:

```python
greet()
```

without passing a value, Python uses `"Varun"`.

---

## Passing Our Own Value

```python
def greet(name="Varun"):
    print("Hello", name)

greet("Rahul")
```

Output:

```text
Hello Rahul
```

When we provide a value, the provided value **replaces the default value**.

```text
greet()
      ↓
name = "Varun"       → default value

greet("Rahul")
      ↓
name = "Rahul"       → provided value
```

---

## Example with Numbers

```python
def add(a, b=10):
    return a + b

print(add(5))
print(add(5, 20))
```

Output:

```text
15
25
```

Explanation:

```text
add(5)
   ↓
a = 5
b = 10  ← default
   ↓
5 + 10 = 15


add(5, 20)
   ↓
a = 5
b = 20  ← provided value
   ↓
5 + 20 = 25
```

## Important Rule

A **default parameter must come after a normal parameter**.

Correct:

```python
def add(a, b=10):
    return a + b
```

Incorrect:

```python
def add(a=10, b):
    return a + b
```

Python gives an error because a non-default parameter cannot come after a default parameter.

## Easy Definition

> **Default parameter = A parameter with a value already assigned. If no argument is provided, the default value is used.**

## Quick Example

```python
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Varun")
```

Output:

```text
Welcome Guest
Welcome Varun
```

### Remember

```text
No argument → Default value is used
Argument given → Given value is used
```