def SoD(n):
    if (n==0):
        return 0
    else:
        return(n%10)+SoD(n//10)
num=int(input("Enter a No:"))
print('Sum of digits is', SoD(num))    