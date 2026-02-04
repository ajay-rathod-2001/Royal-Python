# total=0
# num=int(input("Enter the Any Number: "))
# if num >1:
    
#     for i in range(2,num):
    
#         if num % i ==0:
            
#             print("This is Not prime number")
            
#             break
    
#     else:
        
#         print("Prime number")  
        
               
# print("Prime Number total: ",total)    


total=0

for i in range (2,101):
    
    for j in range(2,i):
        
        if (i%j==0):
            
            break
        
    else:
        total+=i
        
        print(i)  
          
print("Total Prime Number Addition: ",total)           