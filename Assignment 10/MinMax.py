def max_min(lst):
    max = lst[0]
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

lst = [12, 45, 7, 89, 34, 22]
max, min = max_min(lst)
print("List:", lst)
print("Maximum element:", max)
print("Minimum element:", min)
