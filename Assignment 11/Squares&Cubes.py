n = int(input("Enter a No:"))
numbers = []
squares = []
cubes = []

for i in range(1, n+1):
    numbers.append(i)
    squares.append(i*i)
    cubes.append(i*i*i)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
