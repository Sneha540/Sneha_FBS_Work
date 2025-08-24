def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_of_series(n):
    if n == 1:
        return 1
    else:
        return factorial(n) + sum_of_series(n - 1)
n = int(input("Enter the number: "))
result = sum_of_series(n)
print("Sum of series 1! + 2! + ... +", n, "! =", result)
