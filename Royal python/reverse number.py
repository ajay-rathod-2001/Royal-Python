num=int(input("Enter the Any long Digit Number: "))

rev=0

while num>0:
    
    reminder=num % 10
    
    rev= rev * 10 + reminder
    
    num = num // 10
    

print("Rverse Number is : ",rev)