# Café Management System - Shifa's Delight

menu = {
    "Pizza": 140,
    "Burger": 100,
    "Pasta": 120,
    "Fries": 60,
    "Cheesecake": 150,
    "Donut": 70,
    "Coffee": 60
}

print("Welcome to Shifa's Delight Café!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

order = []
total = 0

while True:
    item = input("Enter item name to order (or type 'done' to finish): ").title()
    if item == 'Done':
        break
    if item in menu:
        order.append(item)
        total += menu[item]
        print(f"Added {item} - ₹{menu[item]}")
    else:
        print("Sorry, we don't have that item.")

print("Order Summary:")
for item in order:
    print(f"- {item}: ₹{menu[item]}")
print(f"Total Bill: ₹{total}")
