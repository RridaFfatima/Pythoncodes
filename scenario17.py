name=input("enter your name: ")
tablenumber=int(input("Enter a table number: "))
noofquestions=int(input("enter the number of questions: "))
while(tablenumber<=0):
    tablenumber=int(input("Invalid entry, enter again: "))
while(noofquestions<=0):
    noofquestions=int(input("Invalid entry, enter again: "))
correct=0
incorrect=0
for i in range(1,noofquestions+1):
    answer=int(input(str(tablenumber)+ "x" +str(i)+ "="))
    result=tablenumber*i
    if(answer==result):
        print("correct answer")
        correct=correct+1
    else:
        print("incorrect answer, correct answer is",result)
        incorrect=incorrect+1
percentage=(correct/noofquestions)*100
print("-"*40)
print("perfromance report: ")
print("-"*40)
print("name: ",name)
print("table number: ",tablenumber)
print("no of questions: ",noofquestions)
print("correct answers: ",correct)
print("incorrect answers: ",incorrect)
print("percentage: ",round(percentage,2))
if(percentage<=50):
    print("bad result")
elif(percentage==100):
    print("excelent result")
elif(percentage>50):
    print("good result")
else:
    print("bad result")
