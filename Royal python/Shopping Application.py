print("WelCome to the PR Shopping Mall ")

print("""

1.Electronics

2.Clothing

3.Groceries

4.Exit      
      """)

choice= int(input("Enter the Your Choice:"))

if choice==1:
    
    print("""
          
          1.Mobile(25000 RS
          
          2.Laptop(55000 Rs)
          
          3.TV    (35000 RS)
          
          4.Exit
          """)
    choice1=int(input("Enter the Your choice:"))

    if choice1==1:
        
        price=25000
        
        print("You Have Selected Mobile")
        
    elif choice1==2:
        
        price=55000
        
        print("You Have Selected Laptop")
        
    elif choice1==3:
        
        price=35000
        
        print("you have Selected Tv")
        
    elif choice1==4:
        
        print("Thans For Visiting RR Shopping Mall, \n Have Nice Day....!")
        
    else:
        
        print("Invalid Your Choice Dear Customer...!")
        
elif choice==2:
    
    print("""
          
          1.Shirt(400 Rs)
          
          2.Pant(500 RS)
          
          3.T-Shirt(250 RS)
          
          4.Exit
          
          """ )
    
    choice2=int(input("Enter the Your Choice: "))
    
    if choice2==1:
        
        price=400
        
        print("You have Selected Shirt")
        
    elif choice2==2:
        
        price=500
        
        print("You have Selected Pant")
        
    elif choice2==3:
        
        price=250
        
        print("you have selected t-shirt")
        
    elif choice2==4:
        
        print("Thanks for Visiting PR Shopping Mall, \n Have Nice Day...!")
        
    else:
        
        print("Invalid Your Choice Dear Customer....!")
        
elif choice==3:
    
    print("""
          
          1.Rice(40 rs per kg)
          
          2.Sakhar(50 rs per kg)
          
          3.Nirma(65 rs per kg)
          
          4.Exit
          """)
    
    choice3=int(input("Enter the Your Choice: "))
    
    if choice3==1:
        
        price=40
        
        print(" You have Selected Rice")
        
    elif choice3==2:
        
        price=50
        
        print("You have Selected Sakhar")
        
    elif choice3==3:
        
        price=65
        
        print("You Have Selcetd Nirma")
    
    elif choice3==4:
        
        print("Thanks for Vising PR SHopping Mall")
        
    else:
        
        print("Invalid Choice Dear customer...!")
        
elif choice==4:
    
    print("Thanks for Visitnig PR Shopping Mall, \n Have A GrateFull Day....!")

else:
    
    print("Ivalid choice Dear customer")
    
quantity=int(input("Enter the Your Quantity: "))

total=price*quantity

if total >30000:
    
    discount=total*0.15

    print("You have got 15% discount ")
    
elif total < 15000:
    
    discount=total*0.10
    
    print("you got 10% discount")
    
else:
    
    discount=0
    
    print("Sorry... \n No Discount For you ") 
    
finalAmount=total - discount

print("you got discountof Rs",discount)

print("your Final Amount is : " ,finalAmount)

print("Do Visit Again...! \n PR Shopping MAll")  
    
