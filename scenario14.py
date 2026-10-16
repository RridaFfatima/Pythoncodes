print("Daily Temperature Monitoring")
days=int(input("Enter the number of days that will be monitored: "))
while(days<=0):
    days=int(input("INVALID, Enter again: "))
temp_above_35=0
temp_below_10=0
temp_between_10and35=0
sum=0.0
for i in range(1,days+1):
    temperature=float(input("Enter the temperature for day "+str(i)+": "))
    sum=sum+temperature

    if(i==1):
        highest=temperature
        lowest=temperature
    else:
        if(temperature>highest):
            highest=temperature
        if(temperature<lowest):
            lowest=temperature
    if(temperature>35):
        temp_above_35=temp_above_35+1;
    if(temperature<10):
        temp_below_10=temp_below_10+1
    if(temperature>=10 and temperature<=35):
        temp_between_10and35=temp_between_10and35+1
average=sum/days
print("Report: ")
print(" Number of monitored days: ",days)
print(" Average temperature: ",average)
print(" Highest temperature: ",highest)
print(" Lowest temperature: ",lowest)
print(" Days with temp above 35C: ",temp_above_35)
print(" Days with temp below 10C: ",temp_below_10)
print(" Days with temp between 10C and 35C: ",temp_between_10and35)

    
