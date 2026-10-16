name=input("Enter your name: ")
dailywage=float(input("Enter your daily wage: "))
present=0
absent=0
for days in range (0,26):
    while True:
        attendane=input("enter your attendance (P/A): ")
        attendane=attendane.upper()
        if(attendane=='P'):
            present=present+1
            break;
        
        elif attendane=='A':
            absent=absent+1
            break;
        else:
            print("Invalid entry,enter again")
salary=present*dailywage
attendane_percentage=(present/26)*100

print("Attendance and Salary summary")
print("-"*40)
print("Name: ",name)
print("total presents: ",present)
print("total absents: ",absent)
print("Attendance percentage: ",round(attendane_percentage,2))
print("Salary: ",salary)

if(attendane_percentage<80):
    print("warning attendance is below 80%")
else:
    print("attendance is good")