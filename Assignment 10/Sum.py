def sum_of_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

lst = [10, 20, 30, 40, 50]
print("List:", lst)
print("Sum of elements:", sum_of_list(lst))
