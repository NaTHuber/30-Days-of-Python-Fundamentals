# Day 11. Error handling
## Today's objective 
Learn how to handle errors in Python using exceptions. Understand why error handling is important for building reliable programs, and practice using `try`, `except`, `else`, and `finally`.

## Explanation 
Errors or exceptions happen when something unexpected occurs while your program runs.

**Example**

```python
print(10 / 0)  # ZeroDivisionError
```
Without handling, Python stops execution. To avoid crashes, It 's used exception handling:

```python
try:
    x = int('Hallo')
except ValueError:
    print("You must enter a number.")
```

We can handle multiple exceptions 

```python
try:
    x = int(input('write a number (no cero)'))
    result = 10/x
except ValueError:
    print("Invalid, you must enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero." )
``` 

`else` and  `finally`

```python
try:
    num = 5
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero error.")
else:
    print("Result:", result)   # runs if no exception
finally:
    print("This always runs.")  
```

The `finally` block is a part of exception handling that always executes, no matter what happens in the try or except blocks. Its main purpose is to ensure that cleanup code runs (like closing files, releasing resources, or disconnecting from a database).

## Small note 
> Error handling is essential in real-world applications whether it’s validating user input, working with files, or making sure a program doesn’t crash unexpectedly. A good rule of thumb: anticipate errors you expect, and handle them 🌱