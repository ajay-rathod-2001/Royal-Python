file=open("Intro.txt","r")
data=file.read()

print("data of the file is : ",data)

file=open("certificate.txt","r")
datafile=file.read()

datafile=datafile.lower()

if "live" in datafile:
    print(" yes! Live words is present in the file")
else:
    print("No! Live  file")
    

print("Practice 2 \n")

#Write Mode :

file=open("report222.txt","x")
file.write(" Python learning is Starting very joyfull and all set")