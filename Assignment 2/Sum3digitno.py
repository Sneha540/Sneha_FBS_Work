number = int(input("Enter a three-digit number: "))
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
sum_of_digits = hundreds + tens + ones
print(f"The sum of digits of {number} is: {sum_of_digits}")