# main Dataset Preparation file

import xlsxwriter, sys
from typing import Callable
from itertools import repeat
from Modules.aadhar_number import Aadhar_Number
from Modules.names import get_names
from Modules.vaccination import vaccination_dates

book = xlsxwriter.Workbook("Vaccination_data.xlsx")
sheet = book.add_worksheet()
print("Writting into the file. Please Wait....")

row = 0; column = 0
dataset =100000

content = ["Aadhar_Number", 
           "Name", 
           "Vaccination_Date(1st Dose)", 
           "Day_Gap",
           "Vaccination_Date(2nd Dose)",
           "Day_Gap(in months)",
           "Vaccination_Date(Booster Dose)",
           "Partially_Vaccinated",
           "Fully_Vaccinated",
           "Booster_Vaccinated",
           "Vaccine_Name",
           "State/U.T",
           "Vaccination Certified"
           ]

# Iterating through the content list
print("Writting the headings first...\n")
for item in content:
    sheet.write(row,column,item)
    column +=1
if column == len(content):
    print("Heading written Successfully..!")
    print("Now writting the Data for each column...\n")
    
def write_columns(row:int, column:int, content_name:str, function: Callable)->None:
    listings = []
    print(f"Now writting for the column number{column} for the heading '{content_name}'.")
    for i in range(dataset):
        listings.append(function())
    for i in listings:
        sheet.write(row,column,i)
        row +=1
    print(f"The Data for the Column number{column} for the heading '{content_name}'.Written Successfully!")

row, column =1, 0 # Aadhar Number
write_columns(row, column, content[0], Aadhar_Number)  

row, column =1, 1 # Names
write_columns(row, column, content[1], get_names)
print("\nWritting Data in other columns too...\n")

row, column =1, 2 # Vaccination Date (1st Dose)


book.close()
print("\nDone")
print("\nNow Saving the File.Please Wait.....!\nDont't Shut the Program.")
