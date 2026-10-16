print("Public Transport Fare Estimator")
print("-"*40)
name=input("enter your name: ")
age=int(input("Enter your age: "))
distance=float(input("Enter your travel distnce: "))
if(age<0):
    print("invalid age")
elif(distance<=0):
    print("invalide distance, not applicable")
else:
    if(distance<=5):
        fare=50
    elif(distance>=5 and distance<=15):
        fare=100
    elif(distance>=15 and distance<=30):
        fare=180
    else:
        fare=250
    if(age>=60):
        discount=fare*0.20
    else :
        discount=0
    finalfare=fare-discount
    print("-"*40)
    print("name: ",name)
    print("age: ",age)
    print("travel distance: ",distance)
    print("base fare: ",fare)
    print("discount: ",discount)
    print("final fare: ",finalfare)
print("-"*40)