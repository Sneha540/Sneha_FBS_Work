def second_largest(lst):
    lst = list(set(lst))      
    lst.sort()                
    return lst[-2]            

lst = [12, 45, 7, 89, 34, 22]
print("List:", lst)
print("Second largest element:", second_largest(lst))

