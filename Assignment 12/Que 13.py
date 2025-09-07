s = "She got 98 marks in English"
letters = 0
digits = 0

for ch in s:
    if '0' <= ch <= '9':  
        digits += 1
    elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'): 
        letters += 1

print("String:", s)
print("Letters:", letters)
print("Digits:", digits)
