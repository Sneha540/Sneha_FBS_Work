import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

D = b**2 - 4*a*c

if D > 0:

    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"\nTwo distinct real roots: {root1:.2f} and {root2:.2f}")
elif D == 0:
    
    root = -b / (2*a)
    print(f"\nTwo equal real roots: {root:.2f}")
else:
    
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print(f"\nTwo complex roots: {real_part:.2f} + {imaginary_part:.2f}i and {real_part:.2f} - {imaginary_part:.2f}i")
