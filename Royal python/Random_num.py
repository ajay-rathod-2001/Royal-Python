import random
number=random.randint(1, 100)

print(" u have only three attempts to Guess the Number")

print(" Guess the number Between 1 to 100")

attemps=3

for i in range(1,attemps+1):
    
    guess=int(input("Enter ur guess : "))
    
    
    
    if guess < number :
        print("Too High")
        
    elif guess > number:
        print("Very High")
    
    else:
        print(" Your Guess is Right ")
        break
else:
    print(f" you have exhausted all ur attempts. The Number was { number}")
            
        
    