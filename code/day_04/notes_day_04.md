# Day 04. Conditionals 
## Today's objetive
Understand how to use conditional statements in Python to control the flow of a program based on logical conditions.

---

## What conditionals do?
Conditionals allow a program to make decisions. They let you execute certain blocks of code only if specific conditions are true.

The most common key words are:

- `if`
- `elif`
- `else`

## Basic syntax 

```python
if condition:
    # code runs if condition is True
elif another_condition:
    # code runs if previous condition is False and this one is True
else:
    # code runs if all above conditions are False
```

## Examples 
In the following example you check if the temperature is greater than 25°C, in this case you will print _It's hot outside_

```python 
temperature = 30
if temperature > 25:
    print("It's hot outside")
```

Let's use `else`

```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Let's use `elif`

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")
```

You can use more than one conditional 

```python
number = 20
if number > 10:
    if number % 2 == 0:
        print('Your number is greater than 10 and even')
    else:
        print('Your number is greater than 10 and odd) 
```

## Comparison and logical operators 
You can combine conditions with:

- `and` **Both conditions must be True**

- `or` **At least one condition must be True**

- `not` **Negates a condition**

Example

```python
x = 5
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

---

## Small note
> Conditionals are the backbone of decision-making in programs. They help in adapting the program’s behavior to different inputs and situations 🌱