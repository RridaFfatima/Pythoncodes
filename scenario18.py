noofemployees=int(input("How many employees will be added in the report: "))
totalsales=0
count=0
highestsales=0
highestname=""
tie=False
for i in range(noofemployees):
    name=input("enter employee name: ")
    amount=float(input("enter amount: "))
    while(amount<0):
        amount=float(input("invalid entry, enter again: "))
    print("employee: ",name," sales: Rs.",amount)
    totalsales=totalsales+amount
    if(amount>=10000):
        count=count+1
    if(amount>0 and amount>highestsales):
        highestsales=amount
        highestname=name
        tie=False
    elif(amount==highestsales):
        tie=True
print("Total shop sales: Rs.",totalsales)
if(noofemployees>0):
    average=totalsales/noofemployees
    print("average sale per employees: ",round(average,2))

    if(tie==True):
        print("highest sale at: Rs.",highestsales)
        print("more than one highest sale employee")
    else:
        print("highest sale at: Rs.",highestsales)
        print("highest sales emaployee name: ",highestname)
print("employees reaching the target 10,000: ",count)   