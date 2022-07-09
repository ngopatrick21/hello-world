
product_name = input("Enter name of item: ")

product_price = float(input("Enter price of " + product_name + ': '))

product_sold = float(input("Enter quantity of " + product_name + " sold: "))

# print(product_name)
# print(product_price)
# print(product_sold)
print("")
print(product_name + " sales")
print("Quantity Sold: " + str(product_sold))
print("Unit Price: " + str(product_price))

total = product_price * product_sold

print("Total: " + str(total))

