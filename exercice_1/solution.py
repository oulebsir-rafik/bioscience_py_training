"""Contains solution for exercice 1."""
with open("data.txt") as f:
    data = f.read()

data = data.split("//")
data = [d.strip() for d in data]
print(data)
print("############################################")
data = [d.split("\n") for d in data]
# get the price, the name and the quantity
data_processed = []

for d in data:
    d[1] = d[1].replace(" ", "")
    d[2] = d[2].replace(" ", "")
    d[0] = d[0].replace(" ", "")

    price = d[0].split("Price:")[1]
    product = d[1].split("Product:")[1]
    qty = d[2].split("Quantity:")[1]

    data_processed.append({"price": price, "product": product, "quantity": qty})

print(data_processed)
