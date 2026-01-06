
cart = [('bed', 200.0), ('cat', 100.0), ('kitchen', 4000.0), ('milk', 2.5), ('5', 5.0)] 

cart.remove(cart[0])

print(cart)

total = 0
for price  in cart:
    total += price[1]

print("Total: $", total)


