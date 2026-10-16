total=0
name=input("Enter customer name: ")
while True:
    print("-"*40)
    print("Cafeteria Menu: ")
    print("-"*40)
    print("Items    ", "Price")
    print("1. Sandwich    ","Rs.250")
    print("2. Burger   ","Rs.400")
    print("3. Pizza Slice   ","Rs.300")
    print("4. Juice   ","Rs.120")
    print("-"*40)
    item=int(input("Enter number of item(1-4): "))
    quantity=int(input("Enter quantity of the selected item: "))
    if item<1 or item>4:
        print("invalid menu selection") 
    elif quantity<=0:
        print("Invalid Quantity")
    else:
        if item==1:
            item_name="Sandwich"
            price=250
        elif item==2:
            item_name="Burger"
            price=400
        elif item==3:
           item_name="Pizza Slice"
           price=300
        elif item==4:
           item_name="Juice"
           price=120
        subtotal=price*quantity
        
        if subtotal>=1000:
            discount =0.1*subtotal
        else:
            discount=0
        finalbill=subtotal-discount
        total=total+finalbill
        print("-"*20,"Receipt","-"*20)
        print("customer name: ",name)
        print("selected item: ",item_name)
        print("Quantity per item:  ",quantity)
        print("Subtotal: ",subtotal)
        print("discount: ",discount)
        print("final bill: ",finalbill)
        print("-"*40)
    input_choice=input("get another item (yes/no): ")
    if input_choice.lower()!="yes":
        break;
print("your grand total is: ",total)
print("Thankyou!")


