cart = []
item = input()
a = 0
while item != "":
    cost, quant = map(int, item.split())
    cart.append(cost * quant)
    a += cost * quant
    item = input()
for i in cart:
    print(i)
print("Сумма: ", a)
