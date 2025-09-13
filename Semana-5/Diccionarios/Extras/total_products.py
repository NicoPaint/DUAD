products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

results = {}

for product in products:
    if(results.get(product.get("category"))):
        results[product.get("category")] += product.get("price")
    else:
        results[product.get("category")] = product.get("price")

print(results)