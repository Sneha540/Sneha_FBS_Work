def cube_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i ** 3)
    return new_list

lst = [1, 2, 3, 4, 5]
print("Original List:", lst)
print("List with cubes:", cube_list(lst))
