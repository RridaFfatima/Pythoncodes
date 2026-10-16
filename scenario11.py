number=55
name=input("Enter your name: ")
attempts=0
while attempts<7:
    guess=int(input("Enter your guess: "))
    if(guess<1 or guess>100):
        print("invalid, out of range, enter between 1 and 100")
    attempts=attempts+1
    if(guess==number):
        print("Guess Successful!")
        print("number of attempts: ",attempts)
        break;
    elif(guess<number):
        print("Guess too low")
    else:
        print("Guess too High")
if(attempts==7 and guess!=number):
    print("the game is over! You have used all your seven attempts")  
    print("The secret number is: ",number)