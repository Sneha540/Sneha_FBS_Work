def power_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + power_sum(num // 10, power)

def is_armstrong(num):
    digits = len(str(num))
    return num == power_sum(num, digits)
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")



