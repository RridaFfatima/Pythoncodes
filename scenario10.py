name =input("Enter your name: ")
current_balance=float(input ("enter your current balance: "))
successful_withdrawals=0
total_withdrawal_amount=0
while True:
    withdrawal_amount=float(input("Enter the amount to withdraw: "))

    if(withdrawal_amount<0):
        print("invalid amount to withdraw")
    elif(withdrawal_amount%500!=0):
        print("invalid amount , enter a multiple of 500")
    elif(withdrawal_amount>current_balance):
        print("Insufficient balance")
    else:
        current_balance=current_balance-withdrawal_amount
        successful_withdrawals=successful_withdrawals+1
        total_withdrawal_amount=total_withdrawal_amount+withdrawal_amount
        print("Transaction Succesful")
        print("withdrawl amount: ",withdrawal_amount)
        print("current balnce: ",current_balance)

    input_choice=input("want to do more transaction(yes/no): ")
    if(input_choice.lower()=="no"):
        print("Customer name: ",name)
        print("Current Balance: ",current_balance)
        print("succesful withdrawals: ",successful_withdrawals)
        print("total amount withdrawn: ",total_withdrawal_amount)
        print("Thankyou!")
        break;


