def SoN(n):
    if (n==0):
        return 0
    else:
        return(n%10)+SoN(n//10)
num=int(input("Enter a No:"))
print('Sum of numbers is', SoN(num))