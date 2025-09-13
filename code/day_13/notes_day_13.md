# Day 13. Strings and useful methods
## Today's objective 
Learn how to work with strings in Python, exploring their properties, common operations, and built-in methods that make text manipulation easier.

## Explanation 

### Strings Basics
- Strings are sequences of characters enclosed in quotes (`'`, `"`, or `"""` for multi-line).
- Strings are immutable: once created, they cannot be changed, any modification creates a new string.

```python
text = "Python"
print(text[0])   # 'P'
print(text[-1])  # 'n'
```
### Concatenation and Repetition
```python
greeting = "Hello"
name = "Alice"
print(greeting + " " + name)  # "Hello Alice"
print("Hi! " * 3)             # "Hi! Hi! Hi! "
```

### Useful String Methods

Some of the most used ones:

- `.lower()`, `.upper()`, `.title()`, `.capitalize()`
- `.strip()`, `.lstrip()`, `.rstrip()`
- `.replace(old, new)`
- `.split(separator)` and `.join(iterable)`
- `.find(substring)`, `.count(substring)`
- `.startswith()`, `.endswith()`

