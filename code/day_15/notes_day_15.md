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
```
def greet(name):
    return f"Hello {name}!"
    
say_hello = greet # Assing function to variable
print(say_hello("Natalia"))
```