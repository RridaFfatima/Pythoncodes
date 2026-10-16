name=input("Enter your name: ")
savings_goal=float(input("Enter your savings goal: "))
initial_savings=float(input("Enter your initial savingss: "))
while(savings_goal<=0):
    savings_goal=float(input("invalid goal, enter again"))

while(initial_savings<=0):
    initial_savings=float(input("invalid savings, enter again"))
total_savings=initial_savings
weeks=0
if(initial_savings>=savings_goal):
    print("savings goal already achieved")
else: 
    while True:
        amount_per_week=float(input("Enter the amount saved this week: "))
    
        if(amount_per_week<0):
            print("invalid entry,enter again")
            continue
        total_savings=total_savings+amount_per_week
        remaining_amount=savings_goal-total_savings
        weeks=weeks+1
        if(remaining_amount<0):
            remaining_amount=0
        print("total savings: ",total_savings)
        print("Remaining amount to reach the target: ",remaining_amount)
        if(total_savings>=savings_goal):
            print("Goal reached!")
            break
        input_choice=input("do you want to continue or stop(yes/no): ")
        if input_choice.lower()=="no":
            break
print("Name: ",name)
print("total savings: ",total_savings)
print("weeks recored: ",weeks)

if(total_savings>=savings_goal):
        print("Goal reached!")
else:
    print("Goal unachieved")
    print("remaining amount: ",remaining_amount)