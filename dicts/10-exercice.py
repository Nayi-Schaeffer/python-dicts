shopping_cart = ["manzanas","choricillos","yogurt",'alitas de pollo',"jugo de naranja", "confor","mantequilla","choricillos",'alitas de pollo',"jugo de naranja", "confor","mantequilla", "plátanos", "manzanas", "yogurt"]

cart_counter = {}

for shop in shopping_cart:
    if shop in cart_counter:
        cart_counter[shop]+= 1

    else:
        cart_counter[shop]=1

print(f"articulos unicos: {len(cart_counter)}")

for shop in shopping_cart:
    print(f"{shop}: {cart_counter[shop]}")

print(f"Articulos totales: {len(shopping_cart)}")


    



