# class 

class vehicle:
    colors = "black"          # attributes
    petrolOrdesel="petrol"
    mileage="10"
    
# Objects :

car=vehicle()
print(car.colors)

bike=vehicle()
print(bike.mileage)

aeroplane=vehicle()
print(aeroplane.mileage)

# created a class for car brand name scoorpio ?

class car:
    brandname = "Scorpio"
    
obj=car()
print("Brand name is -- ",obj.brandname)


# practice

class Laptop:
    brand="default"
    ram=" 8gb"
    prices="1 lacs"
    
laptop1=Laptop()
laptop1.brand="macbook"
laptop1.ram="16GB"
print("Laptop 1 Brand :",laptop1.brand)

laptop2=Laptop()
laptop2.brand="HP"
laptop2.ram="8GB"
laptop2.prices="45000 RS"
print("Laptop2 Brand Name is : ",laptop2.ram)


# Student :

class Student:
    schoolname=" PR School , College and University"
    
    def __init__(self,name,course):
        #print("When a new Object is created called automatically")
        
        self.name=name
        self.course=course
        
        
    
stud=Student("Khushi","BE")    # init method will be called
print("student1 name ",stud.name)
print(" Student1 course",stud.course)

stud1=Student("Harsh","CSE")
print("student2", stud1.name)
print("Student2 ",stud1.course)


        