n = int(input("Enter No.: "))
sum_fact = 0
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum_fact += fact
print("Sum of factorial series:", sum_fact)



##exponent
N = int(input("Enter No.: "))
sum_pow = 0
for i in range(1, N+1):
    sum_pow += N**i
print("Sum of power series:", sum_pow)

##geometric series
n = int(input("Enter number of terms: "))
sum_geo = 0
for i in range(n):
    sum_geo += 2**i
print("Sum of geometric series:", sum_geo)



a = int(input("Enter value of a: "))
S = 0
for i in range(1, 11):
    S += (a**i) / i
print("Sum of the series:", S)


##alternating series
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
S = 0
sign = 1   
den = 1    
for i in range(1, n+1):
    S += sign * (x**i) / den
    sign *= -1
    den += 2
print("Sum of alternating series:", S)