# Write a Python program to find all the anagrams and group them together from a given list of strings.

words = ["sand", "tea", "tab", "ate", "north", "bat"]

groups = {}

for w in words:
    key = "".join(sorted(w))  
    if key in groups:
        groups[key].append(w)
    else:
        groups[key] = [w]

print("Anagram Groups:")
for g in groups.values():
    print(g)

