# Expense Tracker  project :

expse=[] # list of all dictionary for the expenses

print("=== WELCOME TO EXPENSE TRACKER ===")

while True:
    
    print("         ===== MENU =====")
    
    print("1. Add Expenses ")
    print("2. View All Expenses")
    print("3. View Total Kharch")
    print("4.Exit")
    choice = int(input(" Please Enter Ur Choice : "))
    
# Add Expense :
    if choice==1:
        date=input(" which date to expenses : ")
        category=input(" which type to spend money ? (food,travel,makeup,books) : ")
        description=input("Aur Details Dedo : ")
        amt=float(input("Enter The Amount : "))
        
        expense={
            "date":date,
            "category":category,
            "description":description,
            "amt":amt
        }
        expse.append(expense)
        print("\n Done BRO....Expense is Add Successufull")
        
    elif choice==2:
        
        if len(expse)==0:
            print("No expense Added. Go first Expended Some Moneys...")
            
        else:
            print("===== YE UR all EXpenses...!")
            count =1 
            
            for eachexpen in expse:
                print(f"Expense Number {count} -> {eachexpen["date"]},{eachexpen["category"]},{eachexpen["description"]},{eachexpen["amt"]}")
                count=count+1
                
# Vie Total EXpenses :
    elif choice==3:
        total=0
        
        for eachexpen in expse:
            total=total + eachexpen["amt"] 
        print("\n Toatl Expenses = " ,total)
        
# Exit

    elif choice==4:
        print(" ...THANKS To Use  OUR System... ")
        break
    else:
        print(" Invalid Choice ")
        