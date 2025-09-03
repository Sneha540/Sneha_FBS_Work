list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List1:", list1)
print("List2:", list2)

union_list = list1[:]   
for i in list2:
    if i not in union_list:   
        union_list.append(i)
print("Union of two lists:", union_list)
