def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

lst = [1, 8, 1, 7, 8, 2]
print("Original List:", lst)
print("Without Duplicates:", remove_duplicates(lst))
