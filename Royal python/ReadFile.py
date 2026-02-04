# #with keyword :

import os

file=open("report.txt","r")
data=file.read()
file.close()


with open("report.txt","r") as f:
    data=f.read()
    print("file data : " ,data)
    
# # Read Line by Line :

# with open("intro.txt","r") as f:
#     # line1=f.readline()
#     # line2=f.readline()
#     # line3=f.readline()
#     # line4=f.readline()
    
#     # print(line1)
#     # print(line2)
#     # print(line3)
#     # print(line4)
    
#     lines=f.readlines()
#     print(lines)
    
# # bio.txt

# print("\n")

with open("bio.txt","r") as f:
    line1=f.readline()
    print(line1)
    
with open("bio.txt","r") as f:
    listofline=f.readlines()
    print("Numbetr of line  in file : ",len(listofline))
    
    
# os.rename("bio.txt","aaju.txt")

os.remove("aaju.txt")

    

    
    