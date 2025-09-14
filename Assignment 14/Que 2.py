#Write a Python program to remove the intersection of a second set with a first set.

A = {1, 2, 3, 4, 5}
B = {9, 4, 6}

result = set()

for x in A:
    if x not in B:   
        result.add(x)

print("First Set:", A)
print("Second Set:", B)
print("After removing intersection from first set:", result)
