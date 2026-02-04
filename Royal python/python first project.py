age=int(input("Enter the your age: "))

if age>=18 and age<=25:
    
    print(" you are Elibile for admission")
    
    marks=int(input("Enter oyur Marks: "))
    
    if marks>=90:
        
        print("Admission is Successfully bro...")
        
    elif marks < 90 and marks>70:
        
        print( "you need to pay 2lakhs RS for Admission")
        
    elif marks <70 and marks> 50:
        
        print("you need to pay 4 lakhs RS for Admission")
        
    elif marks < 50 and marks >35:
        
        print(" you need to pay 8 lakhs RS for admisson")
        
    else:
        
        print(" You are Not Elibible for Admission ") 
        
else:
    
    print("You Are Not Eligible for Admission Due to Age ")        
    