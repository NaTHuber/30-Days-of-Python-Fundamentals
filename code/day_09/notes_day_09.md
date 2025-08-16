# Day 09. Tuples and Sets 
## Today's objective 
Understand the differences, uses, and benefits of tuples and sets in Python, and practice how to manipulate them effectively.

---

## Tuples

**Definition:** An ordered, immutable collection of items.

**Syntax:** `(item1, item2, item3)`

**Key Features:**
- Ordered (indexable).
- Immutable (cannot be changed after creation).
- Can contain duplicate elements.
- Often used to store fixed collections of data (e.g., coordinates, RGB colors).

**Example**
```python
point = (3, 4)
print(point[0])   # 3
print(point[1])   # 4
```
and you can also **unpack** them:
```python
x, y = point
print(f"x = {x}, y = {y}")
```

## Sets

**Definition:** An unordered collection of unique items.

**Syntax:** `{item1, item2, item3}`

**Key Features:**
- Unordered (no indexing).
- No duplicates allowed.
- Useful for membership tests and removing duplicates.
- Support set operations like union, intersection, and difference.
    ```python
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print(a | b)  # Union -> {1, 2, 3, 4, 5, 6}
    print(a & b)  # Intersection -> {3, 4}
    print(a - b)  # Difference -> {1, 2}
    ```

**Example**
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  # True

# Removing duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}
```

## Small note
> Use tuples when you want fixed collections of data (like coordinates or database keys). Use sets when you need to remove duplicates or perform mathematical-like operations 🌱