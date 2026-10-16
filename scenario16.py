tickets12=0
tickets59=0
tickets60=0
revenue12=0
revenue59=0
revenue60=0


while True:
    age=int(input("enter your age: "))
    if(age<0):
        print("invalid age")
        continue
    if(age<12):
        ticket=300
        tickets12=tickets12+1
        revenue12=revenue12+ticket
    elif(age>=12 and age<=59):
        ticket=600
        tickets59=tickets59+1
        revenue59=revenue59+ticket

    else:
        ticket=400
        tickets60=tickets60+1
        revenue60=revenue60+ticket

    input_choice=input("continue or not(yes/no): ")
    if input_choice.lower()=="no":
         break
totaltickets=tickets60+tickets12+tickets59
totalrevenue=revenue12+revenue59+revenue60
print("No of tickets sold for childern below 12: ",tickets12)
print("No of tickets sold for adults between 12 and 59: ",tickets59)
print("No of tickets sold for seniors above 60: ",tickets60)
print("total tickets sold: ",totaltickets)
print("Total revenue: Rs. ",totalrevenue)
if(totaltickets>0):
    average=totalrevenue/totaltickets
    print("Average ticket price:Rs. ",round(average))
else:
    print("no tickets sold")
