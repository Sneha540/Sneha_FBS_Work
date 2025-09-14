my_dict = {"name": "Sneha", "age": 21, "Branch": "Information Technology"}
key = "age"

found = False
for k in my_dict:
    if k == key:
        found = True
        break

if found:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")
