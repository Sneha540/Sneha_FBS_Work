my_dict = {"a": 'Pencil', "b": 'Eraser', "c": 'Pen'}
key = "c"

new_dict = {}

for k in my_dict:
    if k != key:      
        new_dict[k] = my_dict[k]

print("Original Dictionary:", my_dict)
print("After removing key:", new_dict)
