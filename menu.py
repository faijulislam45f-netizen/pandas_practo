menu = {"pizza": 50, "burger": 30, "pasta": 40, "salad": 20, "soda": 10, "dessert": 25}
print("Welcome to the restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs {price}")
    total = 0
while True:
    Order = input("Please enter the item you want to order (or type 'done' to finish): ").lower()
    if Order == 'done':
        break
    elif Order in menu:
        total += menu[Order]
        print(f"{Order} added to your order. Current total: Rs{total}")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
        more = input("Do you want to order something else? (yes/no): ").lower()
        if more == 'no':
            break
print(f"Your final total is: Rs {total}")
print("Thank you for dining with us!")