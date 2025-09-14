#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

nums = {1, 4, 5, 2, 3, 6, 7}
target = 7

print("Set:", nums)
print("Pairs with sum", target, ":")

for x in nums:
    for y in nums:
        if x < y and x + y == target:   
            print(x, ",", y)
