n = int(input("Enter the value of n: "))

print(f"Integers up to {n} that aren't divisible by 2 or 3:")

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")
