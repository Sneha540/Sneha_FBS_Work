# Given two sets of numbers, write a Python program to find the missing numbers
# in the second set as compared to the first and vice versa.
# Use the Python set.

A = {1, 2, 3, 4, 5}
B = {3, 4, 6, 7}

missing_in_B = set()
missing_in_A = set()

for x in A:
    if x not in B:
        missing_in_B.add(x)

for y in B:
    if y not in A:
        missing_in_A.add(y)

print("First Set:", A)
print("Second Set:", B)
print("Missing in B:", missing_in_B)
print("Missing in A:", missing_in_A)


