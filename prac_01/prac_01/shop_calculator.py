total = 0.00
items = int(input("Number of items: "))
if items > 0:
    for i in range(0, items):
        price = float(input("Price of item: "))
        total += price
    if items > 1:
        print(f"Total price for {int(items)} items is ${total:.2f}")
    else:
        print(f"Total price for {int(items)} item is ${total:.2f}")
