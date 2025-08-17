def sum_of_odds(n):
    sum = 0
    for i in range(1, n+1, 2):  
        sum += i
    return sum

n = int(input("Enter the value of n: "))

print("The sum of odd numbers=", sum_of_odds(n))
