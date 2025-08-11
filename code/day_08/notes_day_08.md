# Day 08. Dictionaries 
## Today's objective 
Understand what dictionaries are, how to create and manipulate them, and when they are the best choice for storing and retrieving data efficiently.

## What is a dictionary? 

A dictionary in Python is an unordered, mutable, and indexed collection of key-value pairs.

- Keys: Must be unique and immutable (e.g., strings, numbers, tuples).
- Values: Can be of any data type and can be duplicated.
- Introduced in Python using {} or the dict() constructor.

## Creating a dictionary 
```python
# Empty dictionary 
my_dictionary = {}

# With values 
person = {
    "name":"Natalia",
    "age":"25",
    "city":"Augsburg"
}
# Using dic()
car = dict(brand="Toyota", model="Corolla", year=2020)
```
## Accessing and modifying data 
```python
print(person["name"])     # Access value by key → Natalia
person["age"] = 26        # Update value
person["country"] = "Germany"  # Add new key-value pair
```
## Useful methods 
```python
person.keys()       # dict_keys(['name', 'age', 'city', 'country'])
person.values()     # dict_values(['Natalia', 26, 'Augsburg', 'Germany'])
person.items()      # dict_items([('name', 'Natalia'), ('age', 26), ...])
person.get("name")  # 'Natalia' (safe access)
person.pop("age")   # Removes key and returns value
```
## Looping through a dictionary 
```python
for key, value in person.items():
    print(f"{key}: {value}")
```
## Nesting dictionaries 
```python
students = {
    "001": {"name": "Bob", "grade": "A"},
    "002": {"name": "Luna", "grade": "B"}
}

print(students["001"]["name"])  # Bob
```

## When to use a dictionary

- When you need fast lookups by a unique key.
- When your data is naturally paired (e.g., username → email).
- When you need flexibility in storing different data types.

## Small note 
> Dictionaries are like mini databases in memory — flexible, fast, and intuitive. In real-world Python projects, you’ll often use them for configurations, API responses (JSON), and data mapping 🌱