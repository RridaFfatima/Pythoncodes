print("Password Strength and validity checker")
while True:
    password= input("enter your password: ")

    len_checker=False
    uppercase_cecker=False
    Lowercase_checker=False
    digits_checker=False
    if len(password)>=8:
            len_checker=True
    for char in password:
        if(char>='A' and char<='Z'):
            uppercase_cecker=True
        if(char>='a' and char<='z'):
            Lowercase_checker=True
        if(char>='0'and char <='9'):
            digits_checker=True
    if(len_checker):
        print("Atleast 8 characters: Satisfied")
    else:
        print("Atleast 8 characters: Missing")
    if(uppercase_cecker):
         print("Atleast 1 uppercase : Satisfied")
    else:
        print("Atleast 1 uppercase : Missing")
    if(Lowercase_checker):
         print("Atleast 1 lowercase: Satisfied")
    else:
           print("Atleast 1 lowercase: Missing")
    if(digits_checker):
       print("Atleast 1 digit: Satisfied")
    else:
     print("Atleast 1 digit: Missing")

    if len_checker and uppercase_cecker and Lowercase_checker and digits_checker:
        print("Pasword meets all requirements ")
        break
    else:
        print("password doesnot meet all requirements ")
    input_checker=input("if u want to continue(yes/no):")
    if input_checker.lower()!="yes":
         print("Password checker stopped")
         break;
print("-" *40)