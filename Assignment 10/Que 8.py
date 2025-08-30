def duplicate_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i)   
    return new_list

lst = [10, 20, 30, 40]
copy_lst = duplicate_list(lst)

print("Original List:", lst)
print("Duplicate List:", copy_lst)

