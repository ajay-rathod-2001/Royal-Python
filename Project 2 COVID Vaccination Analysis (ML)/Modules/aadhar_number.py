# Column 1 : Aadhar Number Generation
import random

def Aadhar_Number():
    try:
        st =" ";j=0
        while j<12:
            a =random.randint(0,9)
            st +=str(a)
            j=j+1
        return st
    except Exception as e:
        print(e)  
        
print(Aadhar_Number())  
        