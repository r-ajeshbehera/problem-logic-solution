# Write a function called say_hello() that prints:

# "Welcome to Python!"

# Then call it.


def say_hello():
    print("welcome to python programming")
say_hello()

# Write a function called greet_user(name) that:

# Takes a name as input(parameter)

# Prints: "Hello, <name>! Have a great day."

def greet_user(name):
    print(f"Hello, {name}! Have a great day.")
greet_user("Rajesh")

# Problem 2: Sum of Squares Calculator
# Write a function sum_of_squares(n) that:

# Takes a number n

# Calculates 1² + 2² + 3² + ... + n²

# Returns the total sum

# Then call it with n = 5 and print the result.

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total
result = sum_of_squares(5)
print(f"The sum of squares from 1 to 5 is: {result}")
