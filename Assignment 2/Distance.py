feet=float(input("Enter the distance n feet:"))
inches=float(input("Enter the remaining distance in inches:"))
total_inches=(feet*12)+inches
meters=total_inches*0.0254
whole_meters=int(meters)
centimeters=(meters-whole_meters)*100
print(f'Distance:{whole_meters}meters and {centimeters:2f} centimeters')