#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings.
# Use Python set data type.
 
strings = ["apple banana apple", "banana orange", "apple orange banana"]
words = []
for s in strings:
    for w in s.split():
        words.append(w)

unique_words = set(words)

for uw in unique_words:
    count = 0
    for w in words:
        if w == uw:
            count += 1
    print(uw, ":", count)
