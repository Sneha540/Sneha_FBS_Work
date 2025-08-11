n = int(input("Enter a number (n):"))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"Sum of series 1 + 2 + ... + {n} = {total_sum}")
