def calculate_total(cart_items):
    if not cart_items:
        return "The cart is empty. Total Price: 0"
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        total_price *= 0.9
    return f"Total Price: {total_price:.2f}"
cart_items = {}
item_count = int(input("Enter the number of items in your cart: "))
for _ in range(item_count):
    item = input("Enter item name: ").strip()
    price = float(input(f"Enter price for '{item}': ").strip())
    cart_items[item] = price
print(calculate_total(cart_items))
