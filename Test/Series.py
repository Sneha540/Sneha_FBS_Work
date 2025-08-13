n = int(input("Enter value of N: "))
series_sum = 0
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    series_sum += i / fact
print(f'Sum of the series =',{series_sum})
