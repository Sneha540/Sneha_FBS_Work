def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [12, 45, 7, 89, 34, 22]
print("Original List:", lst)

sorted_list = bubble_sort(lst)
second_largest = sorted_list[-2]

print("Sorted List:", sorted_list)
print("Second Largest Number:", second_largest)
