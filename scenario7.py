name=input("Enter your name: ")
subtotal=0
totalitems=0
while True:
    print("-"*40)
    product_name=input("Enter the product name: ")
    product_price=float(input("Enter the product price: "))
    product_quantity=int(input("Enter the product quantity: "))
    if(product_price<=0):
        print("invalid price")
    elif(product_quantity<=0):
        print("invalid quantity")
    else:
        itemcost=product_price*product_quantity
        subtotal=subtotal+itemcost
        totalitems=totalitems+product_quantity
       
        print("Product name: ",product_name)
        print("product quantity: ",product_quantity)
        print("product price: ",product_price)
        print("running subtotal: ",subtotal)
        
    if(subtotal>=5000):
            discountrate =10
    elif(subtotal>=2000):
            discountrate =5
    else:
            discountrate=0
    discount=subtotal*(discountrate/100)
    finalprice=subtotal-discount
    inputchoices=input("Continue or not (yes/no): ")
    if inputchoices.lower()=="no":
         finalprice=subtotal-discount
         print("-"*40)
         print(" Final Receipt")
         print("-"*40)
         print("Customer name: ",name)
         print("total quantity: ", totalitems)
         print("subtotal: ",subtotal)
         print("discount rate: ",discountrate)
         print("discount amount: ",discount)
         print("Final bill: ",finalprice)
         break
    
