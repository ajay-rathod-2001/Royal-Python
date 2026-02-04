import random
OTP=""
def generateOtp():
    global OTP
    for i in range(6):
        OTP+=str(random.randint(0,9)); 
        
    return OTP
        
generateOtp()        

def verifyOtpAndLogin(userOtp):
    if OTP ==userOtp:
        print("login SuccessFull...")
    else:
        print("login Failed...")

def main():
    print("Ur OTP for login  is : ",generateOtp())
    
    userOtp=input("Enter the Your otp : ")
    verifyOtpAndLogin(userOtp)
    
main()
    
    