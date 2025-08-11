ticket_price = float(input("Enter the ticket price per person: ₹"))
total_amount = 0  
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    if age < 12:
        cost = ticket_price * 0.70
    elif age > 59:
        cost = ticket_price * 0.50
    else:
        cost = ticket_price

    total_amount += cost
print(f"\nTotal ticket amount for all 5 people: ₹{total_amount:.2f}")
