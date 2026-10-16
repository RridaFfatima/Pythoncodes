print("University eligibility checker")
name = input("Enter your name: ")
intermediate_marks = float(input("Enter your intermediate marks: "))
Total_marks_intermediate = float(input("Enter your total marks: "))
Entrytest_marks = float(input("Enter your entry test marks: "))
Total_marks_entrytest = float(input("Enter your total entry test markss: "))

if intermediate_marks<0 or Total_marks_intermediate<=0 or intermediate_marks>Total_marks_intermediate:
        print("Invalid Intermediate marks")

    

elif Entrytest_marks<0 or Total_marks_entrytest<=0 or Entrytest_marks>Total_marks_entrytest:
        print("Invalid entry test marks")
    
        
else:
        intermediate_percentage=(intermediate_marks/Total_marks_intermediate)*100
        entrytest_percentage=(Entrytest_marks/Total_marks_entrytest)*100
        print("Intermediate percentage: " ,intermediate_percentage,"%")
        print("EntryTest percentage: ", entrytest_percentage,"%")
        if intermediate_percentage>=60 and entrytest_percentage>=50:
            print("Eligible for admission")
        else:
            print("not eligible for admission")
            if intermediate_percentage<60:
                print("intermediate percentage less than 60%, doesnot meet the requiremnets\n")
            if entrytest_percentage<50:
                 print("entrytest percentage less than 50%, doesnot meet the requiremnets\n")

print("-"*80)



    