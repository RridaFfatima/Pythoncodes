print("Library Late-Return Fine Calculator")
name=input("Enter student name: ")
booktitle=input("Enter book title: ")
nooflatedays=int(input("Enter number of days late: "))
if(nooflatedays<0):
    print("Invalid no of days")
elif(nooflatedays==0):
    print("Book title: ",booktitle)
    fine=0
    print("The book was returned on time or early ,no fine is due")
else:
    if(nooflatedays<=5):
        fine=nooflatedays*10
    elif(nooflatedays<=10):
        fine = 5*10 +(nooflatedays-5)*20
    else:
        fine=(5*10) +(5*20)+(nooflatedays-10)*50
    print("students name: ",name)
    print("Book title: ",booktitle)
    print("no of days late: ",nooflatedays)
    print("fine: Rs. ", fine)