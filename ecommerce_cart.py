def tprice(items):
    if not items:
        return "Cart is empty"
    total = sum(items.values())
    if n > 5:
        total= total-(total*0.1)
    return total

cart_items = {}
n = int(input("Enter number of items in your cart: "))
for i in range(1,n+1):
    item = input(f"Enter name of item {i}: ")
    price = int(input(f"Enter price of {item}: "))
    cart_items[item] = price
result = tprice(cart_items)
print("Total Price:",result)