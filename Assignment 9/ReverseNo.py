def reverse_no(num, rev=0):
    if num == 0:
        return rev
    digit = num % 10
    rev = rev * 10 + digit
    return reverse_no(num // 10, rev)

n = int(input("Enter a number: "))
print("Reversed no is:", reverse_no(n))
