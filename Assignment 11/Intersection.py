list1 = [14, 21, 32, 48, 15]
list2 = [14, 15, 36, 67, 48]

print("List1:", list1)
print("List2:", list2)

intersection_list = []
for i in list1:
    if i in list2 and i not in intersection_list:
        intersection_list.append(i)
print("Intersection of two lists:", intersection_list)
