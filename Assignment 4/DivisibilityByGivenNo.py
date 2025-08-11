start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
divisor = int(input("Enter the number to check divisibility: "))
print(f"Numbers between {start} and {end} divisible by {divisor}:")
for i in range(start, end + 1):
    if i % divisor == 0:
        print(i)
