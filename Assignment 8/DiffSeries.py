# a. Sum of 1 + 2 + 3 + ... + n
def sum_natural(n):
    return n * (n + 1) // 2

# Function to find factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# b. Sum of 1! + 2! + 3! + ... + n!
def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

# c. Sum of 1^1 + 2^2 + 3^3 + ... + n^n
def sum_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# Main program
n = int(input("Enter the value of n: "))

print("a. Sum of natural numbers:", sum_natural(n))
print("b. Sum of factorial series:", sum_factorials(n))
print("c. Sum of power series:", sum_power_series(n))
