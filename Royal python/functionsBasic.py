# # Function Basic :

# def sum():

#    a=3
#    b=8
 
#    sum=a+b
#    print(sum)

# sum()

def welcome_message():
    print(" Wel-Come to python prgrammin For world Take of Aii...")

welcome_message()    

def inspire():
    print(" Ur r the master of Destiny : Ajay Rathod")
inspire()

def avg(a,b):
    
    avgvalue=(a+b)/2
    print(avgvalue)
    
avg(5,10)
avg(7,10)
avg(80,98)
avg(2,4)
  
  # default Value
  
def default(a=10,b=90):
     sum=a+b
     print(sum)  
     
default() 

# one More 

def show_age(name="ajay",age=24):
    
    print(f"{name} is {age} year old...")

show_age("saurabh",25)
show_age()
show_age("suraj",23)    

# Reurn Statement ;

def multiply(a=10, b=20):
    return a*b
result=multiply(5,10)
print(result)
    
    
# Square Number :

def sqr(num=10):
    return num**2
print(sqr(5))


# vowel ands count

def Func(userInput):
    
    vowel="aeiouAIOEU"
    
    countvowel=0
    countConsonent=0
    
    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowel:
                countvowel=countvowel+1
            else:
                countConsonent+=1
                
    return countvowel,countConsonent

vowel,consonent=Func("Ajay Indal Rathod")
print(vowel,consonent)