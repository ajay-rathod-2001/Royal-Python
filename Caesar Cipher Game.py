#Caesar Cipher Encyption and Decryption :



print("""_________                                      _________ .__       .__                  
\_   ___ \_____    ____   ___________ _______  \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \ /    \  \/|  \____ \|  |  \_/ __ \_  __ \
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  (____  /\___  >____  >(____  /__|     \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/      \/                \/   |__|        \/     \/       
""")
      


def encrypt_or_decrypt(original_text,shift_count,option):
    
    secret_code = ""
    
    if option == "decrypt" :
        shift_count *= -1
    
    for letter in original_text:
        
        if letter not in alphabets:
            secret_code += letter
        
        else:
            index_letter = alphabets.index(letter) + shift_count
            
            index_letter = index_letter %  len(alphabets)
            
            secret_code += alphabets[index_letter]
            
    print(f"The {user_input}ed text is : "+secret_code)
    
continue_again=True

while continue_again:
    
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    user_input=input(" Encrypt Or Decrypt : ").lower()

    text=input("Enter the Text : ").lower()

    shift_number=int(input("Enter the Shift Number : "))

    encrypt_or_decrypt(shift_count=shift_number , original_text=text, option=user_input)
    
    ask =input("Do you want to Continue ? Yes/No : ".lower())
    
    if ask == "No" :
        continue_again = False
        print(" Good Bye...!")