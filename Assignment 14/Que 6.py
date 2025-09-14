# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers.
# Use the Python set.

nums = [5, 2, 3, 10, 4, 6]

max_product = float('-inf')
pair = ()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        product = nums[i] * nums[j]
        if product > max_product:
            max_product = product
            pair = (nums[i], nums[j])

print("Pair with maximum product:", pair)
print("Maximum Product:", max_product)
