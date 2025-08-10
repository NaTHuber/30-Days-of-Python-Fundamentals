# Day 07. Lists and list comprehensions 
## Today's objetive
Understand Python lists, their operations, and how to use list comprehensions to write cleaner and more efficient code.

---

## List in Python 
A list is an ordered, mutable (changeable) collection of items.

```python
# Empty list
my_list = []

# List with elements
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# From a range
numbers = list(range(5))  # [0, 1, 2, 3, 4]
```
### Accesing items 
```python
fruits[0]     # 'apple'
fruits[-1]    # 'cherry'
```
### Modifying Lists
```python 
fruits[1] = "blueberry"   # Change element
fruits.append("date")     # Add at the end
fruits.insert(1, "kiwi")  # Insert at index 1
```
### Removing Items
```python
fruits.remove("apple")  # Remove by value
fruits.pop(0)           # Remove by index
del fruits[0]           # Delete by index
fruits.clear()          # Empty the list
```
### Other useful methods 
```python
numbers = [4, 2, 9, 1]
numbers.sort()           # [1, 2, 4, 9]
numbers.reverse()        # [9, 4, 2, 1]
len(numbers)             # 4
```

---

## List Comprehensions
A list comprehension is a concise way to create lists.

### Basic structure 
```python
[expression for item in iterable if condition]
```
### Examples 
```python
# Square numbers 0–9
squares = [x**2 for x in range(10)]

# Even numbers from a list
evens = [x for x in range(10) if x % 2 == 0]

# Words longer than 3 letters
words = ["hi", "hello", "sun", "world"]
long_words = [w for w in words if len(w) > 3]

# Convert to uppercase
upper_fruits = [fruit.upper() for fruit in ["apple", "banana"]]

```

## Small note 
> List comprehensions are not just shorter; they are often faster than traditional for loops. But remember: if the logic becomes too complex, a normal loop might be more readable 🌱