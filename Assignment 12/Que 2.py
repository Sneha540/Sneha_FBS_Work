s = "python"
n = 5
new_str = ""

for i in range(len(s)):
    if i != n:
        new_str += s[i]

print("Original String:", s)
print("After removing index", n, ":", new_str)
