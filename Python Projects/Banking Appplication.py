pin =121212

userPin=int(input("Enter your Pin Number Correctly: "))

if userPin==pin:
    
    print(" Your Pin verified SuccessFully")
    
    print("WelCome to Your PR Bank")
    
    print("""
1.Deposit
2.Withdraw
3.Balance Check
4.Exit          
        """  )
    
    Balance=50000
    
    choice=int (input("Enter the Your choice: "))
    
    if choice==1:
        
        deposite=float(input("Enter the Your Amount to be Deposited: "))
        
        if deposite > 0 :
            
            Balance +=deposite
            
            print("RS",deposite,"has Been Deposite Successfully,\n New Balance is Rs",Balance)
            
        else:
            
            print("Invalid Amount to Deposite")
            
    elif choice==2:
        
        withdraw=float(input("Enter the Your Amount to be Withdraw: "))
        
        if withdraw > 0:
            
            if withdraw <= Balance :
                Balance -=withdraw 
                
                print("Rs","Withdraw Hass Been Successfully, New Balance is Rs",Balance )
                
            else:
                
                print("Insufficient Balance to Withdraw")
                
        else:
            
            print("Your Balance is  RS",Balance)
            
    elif choice==3:
        
        print("Your Balance is Rs",Balance)
        
    elif choice==4:
        
        print("Thanks You for Visting PR Bank")
        
    else:
    
         print("Invalid Choice")
    
else:
    
    print("Incorrect Pin Number....Please Try Again")   
    
    
    
    
    
            
            
            
            
    
    
    
    
