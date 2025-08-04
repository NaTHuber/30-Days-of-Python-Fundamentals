# Day 3 - Input, Comments, and Conventions.
## Today's objetive 
Understand how to interact with the user via input, document your code with comments, and follow naming and formatting conventions to write clean and readable Python code.

---


## Getting data from the user - `input()`
The `input()` function allows user interaction:
```python
name = input('What is your name')
print('Nice to meet you', name)
```
**All data from `input()` is returned as an string. You often have to convert it to `int` or `float`, etc.**

In the following example we convert the input to a integer:

```python
age = int(input('How old are you?'))
print('This is your age plus one year', age + 1)
```


## Comments - Explaining code 
Comments are ignored by the intepreted but they are super essential for understanding.

- **Single line comments:** Start with `#`
- **Multi-line (docstrings):** Use tripe quotes ` ''' ` or ` """ `

For example using `#`

```python 
# This code ask you for the current year and prints the next year
 year = int(input('what is the current year?'))
 print('Next year will be: ', year + 1)
```
and using ` ''' `
 ```python 
 ''' This code ask you for the current year and prints the next year
 '''
 year = int(input('what is the current year?'))
 print('Next year will be: ', year + 1)
 ```
 
 
 ## Coding conventions - Clean Code  with PEP 8

PEP 8 is the official style guide for Python. Some key rules:

- Use snake_case for variables and functions: `user_name`, `calculate_total()`
- Use PascalCase for class names: `MyClass`, `UserAccount`
- Add spaces around operators: `a = b + c` 
- Use 4 spaces for indentation (not tabs)
- Keep lines under 79 characters
- Add two blank lines between functions, one blank line between methods

---

## Small note 
> We can think of it like that: How can writing clear comments and following conventions help my future-self (or collaborators)?. It's a nice, cool and profesional way to work 🌱