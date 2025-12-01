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

say_hello = greet # Assing function to variable
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