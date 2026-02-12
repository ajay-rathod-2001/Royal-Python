def login(username="Ajay",password="121212"):
    if username=="Ajay" and password=="121212":
    
        return True
    else:
        return False
    


def main():
    username=input("Enter the Ur UserName : ")
    password=input("Enter the PassWord : ")
    
    if login(username,password):
        print("Login Successfull...")
    else:
        print("login Failed...")
        
main()