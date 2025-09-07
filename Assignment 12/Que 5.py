s = "Hello World!"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    for v in vowels:
        if ch == v:
            count += 1

print("String:", s)
print("No. of vowels:", count)
