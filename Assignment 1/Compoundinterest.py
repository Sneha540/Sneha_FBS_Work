P = float(input("Enter the Principal amount (P): ₹"))
T = float(input("Enter the Time in years (T): "))
R = float(input("Enter the Rate of Interest per annum (R): "))
CI = P * ((1 + R / 100) ** T) - P
print(f"\nThe Compound Interest is: ₹{CI:.2f}")
