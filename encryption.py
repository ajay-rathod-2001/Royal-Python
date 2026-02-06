alphabets=["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

user_input=input(" Encrypt Or Decrypt : ").lower()

text=input("Enter the Text : ").lower()

shift_number=int(input("Enter the Shift Number : "))


def encryption(original_text,shift_count):
    
    secret_code=""
    
    for letter in original_text:                    #hello
        
        index_letter=alphabets.index(letter) - shift_count
        
        index_letter= index_letter % len(alphabets)
        
        secret_code +=alphabets[index_letter]
        
    print(secret_code)
        
encryption(original_text=text,shift_count=shift_number)

