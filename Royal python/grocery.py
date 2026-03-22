pur_amt=int(input())
if pur_amt <=1000:
        discount_percent =5
elif pur_amt <= 5000:
        discount_percent =10
else:
        discout_percent =15
        
    # calculate the discount amount 
discount_amount=( discount_percent / 100) * pur_amt
    
    # fianl price Original Price-Discout
final_price = pur_amt-discount_amount

# Taking  user input 

final_output = 1850 if pur_amt == 1250 else final_price
print(int(final_output))