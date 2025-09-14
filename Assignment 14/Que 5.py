#Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "friends", "flight"]

prefix = ""
for i in range(len(min(words, key=len))):
    chars = set(word[i] for word in words)
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break

print("Longest Common Prefix:", prefix)
