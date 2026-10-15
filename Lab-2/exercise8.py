products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1},
]

inventory_value = 0
top = None
top_total = 0
for p in products:
    line_total = p["price"] * p["quantity"]
    print(p["name"], line_total)
    inventory_value += line_total
    if line_total > top_total:
        top_total = line_total
        top = p["name"]

print("Total inventory value:", inventory_value)
print("Highest line total:", top, top_total)
