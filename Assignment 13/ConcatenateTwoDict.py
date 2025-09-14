dict1 = {"a": 'Java', "b": 'Python'}
dict2 = {"c": 'PowerBI', "d": 'Tableau'}

result = {}

for k in dict1:
    result[k] = dict1[k]

for k in dict2:
    result[k] = dict2[k]

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Concatenated Dictionary:", result)
