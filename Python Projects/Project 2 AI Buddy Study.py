# AI Study Buddy:

import datetime
import time

name=input("Swagat Hai!, Enter Youy Name : ")
prhrs=datetime.datetime.now().hour

if 5<=prhrs<=11:
    print("Good Morning ",name)
elif 11<= prhrs <=17:
    print("Good After Noon",name)
elif 17<=prhrs<=20:
    print("Good Evening",name)
else:
    print("Good Night",name)


print("----Namste!🙏 Welcome to Your Buddy  ChatBot🤖!----t")
print("You can ask me basic Questions Type 'bye' to exit from bot")

# ChatBot Memory Creation Of Resposes :

rsps={
    "hello":"Hi, Welcome... to ,How Can Help You..?",
    "how are you":"I am Very Fine ...Thank You..!",
    "who are you":"I am Smart Ai CHatBot...Your Buddy...❤️",
    "motivate me":"Keep Going Your Passion to Work Consistency Daily...👍❤️",
    "happy":"Great...bye To Hear That...",
    "nice to meet you":" Hey...! Thanks to meet me...Such GreatFull For Takl to You...Buddy!😘",
    "todays which skills are required":" Goods Questions Buddy...👌 \n 1. Python plus Ai \n2.Machine Learning and Artificial Intelligence \n3.CyberSecurity \n4.Java With Ai \n5.Data Analysis or Data Analytics and Data Science...\n These Skills More Requried In Future Bro...💕😊",
    "how to reach courses and skills for this":" You Will...Reach the YouTube Channels And Also Buy Different flatform...According to You..😊👍 ",
    "thanks to me suggested":" Welcome... I Always Helps You Buddy...😊💕",
    "bye":"Bye Buddy...! Can Reach Any Time Me ,I'm Availbale for You!"
}

#Method To Get Resposes of ChatoBot :

def getResponseBot(userinput):
    userinput=userinput.lower()
    for eachKey in rsps:
        if eachKey in userinput:
            return rsps[eachKey]
    return " I'M not able to tell that You Yet!...\n       I will learn "    

# Take User Input:
while True:
    
    userinput=input("Please ask Your Question : ")

    rply=getResponseBot(userinput)
    print("Bot Responses : ",rply)

    if "bye" in userinput.lower():
        break