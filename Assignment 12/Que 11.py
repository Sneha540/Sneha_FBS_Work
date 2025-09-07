s = "Welcome to FirstBit Solutions"
new_str = ""

for ch in s:
    if ch == " ":
        new_str += "-"
    else:
        new_str += ch

print("Original String:", s)
print("Modified String:", new_str)