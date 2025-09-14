#Write a Python program to find elements in a given set that are not in another set

A = {1, 2, 3, 4, 5}
B = {3, 4, 6}

result = set()

for x in A:
    if x not in B:
        result.add(x)

print("Set A:", A)
print("Set B:", B)
print("Elements in A not in B:", result)
