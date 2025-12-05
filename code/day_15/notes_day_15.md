# Day 15. Advanced functions 

## Today's objective 
- Understand and use first-class functions, higher-order functions, and lambda expressions.
- Master arguments unpacking (*args, **kwargs).
- Know how to write decorators.
- Learn function annotations and why they matter.
- Build strong intuition for functions as “data” — essential for ML model pipelines, callbacks, and flexible design.

## First-Class Functions 
In python fuctions can be: 
- Assigned to variables 
- Passed as arguments 
- Returned from other functions 
**Example**
```python
def greet(name):
    return f"Hello {name}!"

say_hello = greet
print(say_hello("Natalia"))
```

## Higher-Order Functions
A higher-order function is simply a function that:

- receives another function
    
    **or**

- returns another function

**Example**
```python
def apply_operation(func, value):
    return func(value)

def square(x):
    return x**2

print(apply_operation(square, 5))
```
## Lambda expressions 
Small anonymous functions. 
They are perfect for small one-line transformations 
```python 
square = lambda x: x**2
print(square(8)
```
commonly used in:
- sorted()
- map(), filter()
- Pandas operations 
- Callbacks in ML pipelines 

**Example** Sorting with lambda
```python
students = [("Marcel", 30),("Sol", 10),("Luis",20)] 
students_sorted = sorted(students, key = lambda s: s[1])
print(students_sorted)
```