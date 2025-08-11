cost_price = float(input("Enter the CP:"))
selling_price = float(input("Enter the SP:"))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a PROFIT of ₹{profit:.2f}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"You incurred a LOSS of ₹{loss:.2f}")
else:
    print("No Profit, No Loss.")
