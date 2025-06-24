# 05. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

def create_price_dict():
    user_dict = {}
    num_entries = int(input("Enter number of grocery items: "))
    print("\nEnter grocery items and their prices:-")

    for i in range(num_entries):
        item = input(f"Enter name of grocery item {i + 1}: ")
        price = int(input(f"Enter price of {item}: "))
        user_dict[item] = price

    return user_dict

def create_quantity_dict(items_list):
    print("\nEnter quantity for each grocery item:-")
    quantity_dict = {}

    for item in items_list:
        quantity = int(input(f"Enter quantity for {item}: "))
        quantity_dict[item] = quantity

    return quantity_dict

def count_TotalBill(prices, quantities):
    total_bill = 0

    for item, quantity in quantities.items():
        if item in prices:
            total_bill += prices[item] * quantity
        else:
            print(f"Warning: '{item}' not found in the price dictionary.")

    return total_bill

# --- Main Program ---
grocery_prices = create_price_dict()
grocery_quantities = create_quantity_dict(grocery_prices.keys())

print("\nGrocery Prices:", grocery_prices)
print("Grocery Quantities:", grocery_quantities)

total = count_TotalBill(grocery_prices, grocery_quantities)
print("\nTotal bill: ₹", total)