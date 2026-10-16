
print("Personal Monthly Budget Assistant")
print("-"*40)
name=input("Enter your name: ")
allowance=float(input("Enter your monthly allowance: "))
food=float(input("enter your food expense: "))
transport=float(input("enter your transport expense: "))
internet=float(input("enter your internet expense: "))
books=float(input("enter your books expense: "))
other_needs=float(input("enter your other expense: "))
if(allowance<0 or food<0 or transport<0 or internet<0 or books<0 or other_needs<0):
    print("Invalid,money values cant be negative")
else:
    expenditure=food+transport+books+internet+other_needs
    remaining_balance=allowance-expenditure
    print("-"*40)
    print("monthly budget report")
    print("-"*40)
    print("name: ",name)
    print("total allowance: Rs. ",allowance)
    print("total expenditure: Rs. ",expenditure)
    print("remaining balance: Rs. ",remaining_balance)
    if(allowance>0):
        percentage_spent=(expenditure/allowance)*100
        print("percentage of allowance spent: ",percentage_spent)
        if(percentage_spent>80):
            print("WARNING!!!!! u have spent more than 80% of your allowance")
    else:
        print("percentage of allowance spent: can't calculate as allowance is 0")
    if(expenditure<allowance):
        print("Financial Position: Within Budget")
    elif(expenditure==allowance):
        print("Financial Position: Budget Exhausted")
    else:
        print("Financial Position: Overspending")
print("-"*40)
