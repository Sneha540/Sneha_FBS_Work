number = int(input("Enter a 3-digit number: "))
reverse_number = (number % 10) * 100 + ((number // 10) % 10) * 10 + (number // 100)
if number == reverse_number:
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is NOT a Palindrome.")
