print("Smart Electricity Bill Calculator")
name=input("Enter consumers name: ")
units=int(input("Enter Monthly electricity consumption: "))
if units<0:
    print("invalid units")
else:
    if units<=100:
        bill=units*10
    elif units<=200:
        bill= 100*10+((units-100)*15)
    else:
        bill=(10*100) +(15*100)+((units-200)*20)

print("\nconsumers name: ",name)
print("units consumed:" ,units)
print("total bill: Rs. ",bill)