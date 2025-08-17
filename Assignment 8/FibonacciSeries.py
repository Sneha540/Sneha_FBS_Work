def fibonacci_series(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))

print("Fibonacci series:")
fibonacci_series(n)
