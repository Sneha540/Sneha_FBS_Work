# Input list
lst = [10, 20, 30, 20, 40, 20, 50]
print("Original List:", lst)

x = int(input("Enter element to remove: "))
new_list = []
for i in lst:
    if i != x:
        new_list.append(i)
print("List after removing", x, ":", new_list)
