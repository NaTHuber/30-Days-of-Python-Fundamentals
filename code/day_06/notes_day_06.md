# Day 06. Functions 
## Today's objetive
Understand how to define and use functions in Python, including parameters, return values, scope, and the concept of reusability.

---
## What are functions?
A function is a reusable block of code that performs a specific task 

**You define it once and call it whenever you need it**

## Syntax of a fuction 

```python
def function_name(parameters):
    # block of code
    return result  # (optional)
```
Quick example
```python
# Defining the fuction
def greet(name):
    return print(f"Hello, {name}!")

# Calling it 
greet('Marcel')
```

## Key concepts

| Concept               | Description                           | Example                     |
| --------------------- | ------------------------------------- | --------------------------- |
| **Parameters**        | Inputs passed to the function         | `def greet(name):`          |
| **Return**            | Sends back a result                   | `return a + b`              |
| **Docstring**         | Description of what the function does | `"""Adds two numbers."""`   |
| **Default Arguments** | Parameters with default values        | `def greet(name="friend"):` |
| **Keyword Arguments** | Calling with `name=value`             | `greet(name="Natalia")`     |
| **Variable Scope**    | Where a variable is accessible        | local vs global             |

## Examples 
### Fuction with return 
```python
def square(x):
    return x ** 2

result = square(4)
print(result)
```

### Fuction with a default parameter 
```python
def greet(name='stranger'):
    print(f"Hallo, {name}!")

greet()
greet('Nat')
```

### Fuction with more than one parameter 
```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("dog", "Luna")
```
---
## Small note 
> Functions are the foundation of modular programming, they allow you to break down complex problems into smaller, manageable, and reusable pieces of logic 🌱