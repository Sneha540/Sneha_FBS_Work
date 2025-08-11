marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))
marks4 = float(input("Enter marks of Subject 4: "))
marks5 = float(input("Enter marks of Subject 5: "))
total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100  
print(f"\nTotal Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
