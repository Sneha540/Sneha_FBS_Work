nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in nums:
    if i % 2 != 0:   
        new_list.append(i)

print("Original List:", nums)
print("List after removing even numbers:", new_list)
