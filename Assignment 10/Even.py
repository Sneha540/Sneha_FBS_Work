lst = [10, 15, 20, 25, 30, 35, 40]
print("Original List:", lst)

new_list = []
for i in lst:
    if i % 2 != 0:    
        new_list.append(i)
print("List after removing even numbers:", new_list)
