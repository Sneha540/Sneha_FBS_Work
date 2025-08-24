def check_prime(num, divisor=2):
    if num <= 1:
        return False
    if divisor == num:  
        return True
    if num % divisor == 0:  
        return False
    return check_prime(num, divisor + 1)

n = int(input("Enter a number: "))
if check_prime(n):
    print(n, "is a Prime number")
else:
    print(n, "is Not a Prime number")
        