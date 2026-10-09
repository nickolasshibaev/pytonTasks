products = [
    {"name": "Laptop", "price": 45000, "stock": 5},
    {"name": "Phone", "price": 25000, "stock": 0},
    {"name": "Monitor", "price": 12000, "stock": 10},
    {"name": "Keyboard", "price": 3000, "stock": 20},
]

available = list(filter(lambda product: product["stock"] > 0, products))
names = list(map(lambda product: product["name"], available))
prices = list(map(lambda product: product["price"], available))

for name, price in zip(names, prices):
    print(f"{name}: {price} грн")
