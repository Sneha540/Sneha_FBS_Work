def is_armstrong_no(num):
    temp=num    
    sum=0
    count=0
    temp2=num
    while temp2>0:
        count+=1
        temp2//=10  
    while (temp > 0):
        digit = temp % 10
        sum += digit ** count
        temp //= 10
    if sum == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
n=int(input("Enter a number: "))
is_armstrong_no(n)

