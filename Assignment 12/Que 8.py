s = "Hey! What's Up?"
new_str = ""

for i in range(len(s)):
    if i % 2 == 0:     
        new_str += s[i]

print("Original String:", s)
print("After removing odd index chars:", new_str)
