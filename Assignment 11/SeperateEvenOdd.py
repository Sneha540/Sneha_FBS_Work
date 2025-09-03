lst = [10, 15, 20, 25, 30, 35, 40]
print("Original List:", lst)
even_list = []
odd_list = []

for i in lst:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even List:", even_list)
print("Odd List:", odd_list)
