# # LESSON 10: Writing Smarter, Reusable Functions — with Real Use Cases
# Problem 1: Factorial Calculator
# Write a function factorial(n) that:

# Takes a number n

# Returns the factorial(n * (n-1) * (n-2) * ... * 1)

# If n = 5, the result is 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


factorial_result = factorial(5)
print(f"Factorial of 5 is: {factorial_result}")

# Problem 2: Prime Checker
# Write a function is_prime(n) that:

# Returns True if the number is prime, else False

# A number is prime if it’s only divisible by 1 and itself


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(2,n-1):
        if n % i == 0:
            return False
    else:
        return True
num=is_prime(2)
print(f"Is 2 a prime number? {num}")

'''Problem 1: Count Primes in a Range
Write a function count_primes(start, end) that:

Takes two numbers: start and end

Counts how many prime numbers exist in that range

Returns the count'''
def count_primes(start, end):
    if start < 2:
        start = 2
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count  
start = 1
end = 10
prime_count = count_primes(start, end)
print(f"Number of prime numbers between {start} and {end}: {prime_count}")  

'''Problem 2: List Prime Numbers
Write a function list_primes(n) that:

Returns a list of all prime numbers from 2 to n'''
def list_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
n = 20
prime_list = list_primes(n)
print(f"Prime numbers from 2 to {n}: {prime_list}")
