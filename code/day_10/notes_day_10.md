# Day 10. Modules and `import` 
## Today's objectives

- Understand what modules are in Python and why they are useful.
- Learn the different ways to import modules (entire module, specific functions, aliases).
- Practice using built-in modules like `math`, `random`, and `datetime`.
- Create and use my own custom module to organize code.

## What is a Module?

A module is simply a Python file `.py` that contains code (functions, variables, classes).

**Purpose:** to organize and reuse code.

**Example:** Python’s built-in math module.
```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159... and more haha
```

## Ways to Import

- Import the whole module
    ```python
    import random
    print(random.randint(1, 10))
    ```
- Import specific parts 
    ```python 
    from math import sqrt, pi
    print(sqrt(25))
    print(pi)
    ```
- Import everything (not recommended)
    ```python 
    from math import *
    print(sin(pi/2))   # works, but may cause conflicts :(
    ```
## Creating Your Own Module

For example, you can create a file called `mymath.py` and include 
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```
and then 
```python 
import mymath

print(mymath.add(3, 5))      # 8
print(mymath.multiply(4, 6)) # 24
```

## Small note 
> Modules are like **toolboxes**. Instead of reinventing the wheel, Python lets you reuse code whether it’s your own or part of the massive standard library. Mastering imports makes your programs cleaner, more modular, and scalable 🌱
