s = "Guava and Banana"
new_str = ""

for ch in s:
    if ch == 'a':
        new_str += '$'
    else:
        new_str += ch

print("Original String:", s)
print("Modified String:", new_str)
