start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Numbers between {start} and {end} divisible by 7 and multiple of 5:")

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")
