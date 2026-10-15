def apply_discount(total):
    if total >= 2000:
        return total * 0.9
    return total


cart = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1},
]

total = 0
for item in cart:
    total += item["price"] * item["quantity"]

print("Total:", total)
print("Final amount:", apply_discount(total))
