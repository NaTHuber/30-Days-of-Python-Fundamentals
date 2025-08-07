# Day 05. Loops
## Today's objetive 

Understand and practice the use of `for` and `while` loops in Python, including control statements like `break`, `continue`, and `else`, to efficiently repeat tasks and iterate through data structures.

---

## Explanation 
### `for` loop 
Used to iterate over a sequence (list, tuple, string, dictionary, etc.)

```python
for i in range(5):
    print(i) 
```

We can loop through:
- `range()`
- A list: `for item in my_list:`
- A string: `for char in "hello":`

### `while` loop 
Repeats a block as long as a condition is true.

```python
count = 0
while count <= 5:
    print(count)
    count += 1
```
### `break`
Exits the loop prematurely.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`
Skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `else` with loops
Runs once only if the loop wasn't broken

```python
for i in range(5):
    print(i)
else:
    print('Loop finished successfully')
```

## Small note 
> How can loops help me to automate tasks in real life or future projects? 🌱 