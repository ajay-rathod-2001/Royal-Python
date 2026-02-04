# num =int(input("enter the Number"))
# sum=0
# while num>0:
#     rem=

# Project: calculated the Percentage

def get_marks():
    
    print("Enter the Of All Subjects MArks out of 100 :")
    
    s1=float(input("java : "))
    s2=float(input('CPP: '))
    s3=float(input("C : "))
    s4=float(input("Python : "))
    
    return s1,s2,s3,s4

def calculateTotal(marks):
    return sum(marks)
    
        
# total=calculateTotal()
# print("Totals Marks of Sub : ",total)

def calculatePercentage(totalMarks):
    
    percentage=(totalMarks/500)*100
    
    return percentage

# per=calculatePercentage()
# print(" Your Percentage ", per)

def calGrade(percentage):
    
    if percentage>=90:
        grade="A"
    elif percentage>+80:
        grade="B"
    elif percentage>=70:
        grade="C"
    elif percentage>=60:
        grade="D"
    else:
        grade="E"
    return grade

def main():
    marks=get_marks()
    totalMarks=calculateTotal(marks)
    percentage=calculatePercentage(totalMarks)
    grade=calGrade(percentage)
    
    print("total Marks : ",totalMarks)
    print("Percentage  : ",percentage)
    print("grade       : ",grade)
    print("thnak U")
   
main()
            

