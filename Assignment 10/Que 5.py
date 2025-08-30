def check_element(lst, num):
    count = lst.count(num)   
    if count > 0:
        print(num, "is present in the list", count, "time(s).")
    else:
        print(num, "is not present in the list.")

lst = [10, 20, 30, 20, 40, 20, 50]
print("List:", lst)

n = int(input("Enter a number to search: "))
check_element(lst, n)
