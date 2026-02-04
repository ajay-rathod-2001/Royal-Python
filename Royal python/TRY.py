import os

try:
    with open("intro.txt","r") as f:
        listoflines=f.readlines()
        print(" output of raedlines function : ",listoflines)
        print("number of line in file : ",len(listoflines))
except:
    print("that file dos not exits ")