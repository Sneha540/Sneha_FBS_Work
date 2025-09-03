lst = [[1, 4], [3, 1], [5, 9], [2, 6]]

print("Original List:", lst)
lst.sort(key=lambda x: x[1])
print("Sorted List (by second element):", lst)
