x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x==y==z:
    print("This is an Equilateral Triangle")
elif x==y or y==z or z==x:
    print("This is an issosceles Tringle")
else:
    print("This is a Scalene Triangle")