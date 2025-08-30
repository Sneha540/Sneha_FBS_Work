lst = [10, 12, 15, 20, 24, 30, 36, 40, 60]
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

new_list = []
for i in lst:
    if i % m == 0 and i % n == 0:
        new_list.append(i)

print("Numbers divisible by", m, "and", n, ":", new_list)

