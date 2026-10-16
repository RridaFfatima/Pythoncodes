rows=int(input("Enter the number of rows: "))
seats_per_row=int(input("Enter the number of seats per row: "))

if(rows <=0 or seats_per_row<=0):
    print("Invalid dimensions")
else:
    print("seating plan: ")
    seatnumber=1
    capacity=rows*seats_per_row
    for i in range(rows):
        print("Row ",i+1)
        for j in range(seats_per_row):
            print("Seat number:",seatnumber,end='\t')
            seatnumber=seatnumber+1
        print()

print("Total capacity: ",capacity)
customer_count=int(input("Enter how many customers have arrived: "))
if(customer_count<0):
    print("Invalid entry: ")
elif(customer_count>capacity):
    print("invalid customer count,no more customers can sit")
else:
    unoccupied_seats=capacity-customer_count
    print("Occupied seats: ",customer_count)
    print("Unoccupiedseats: ",unoccupied_seats)