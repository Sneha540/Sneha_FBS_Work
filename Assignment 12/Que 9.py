s = "Have a good day!"
char_count = 0
word_count = 1   

for ch in s:
    char_count += 1
    if ch == " ":
        word_count += 1

print("String:", s)
print("Number of characters:", char_count)
print("Number of words:", word_count)
