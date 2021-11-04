products = input().split()
needed_products = input().split()

dic_product = {}

for i in range(0, len(products), 2):
    dic_product[products[i]] = products[i + 1]

for product in needed_products:
    if product in dic_product:
        print(f"We have {dic_product[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")