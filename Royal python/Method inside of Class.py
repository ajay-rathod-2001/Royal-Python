#  Function or Method inside of class

class vehicles:
    color="Black and White Shine Grey"
    brandname="BMW AND ROLLS ROYACE"
    prices=" 15 crore And 21 crore "
    
    def Feture():
        print("Automatically Self DRive Car Feture and securityless properly Also looking Dashing")

    Feture()

car=vehicles()
print(car.color)
print(car.brandname)
print(car.prices)


# Practice2 :

# create class stident that takes 3 marks and has a method avg :

class stud:
    
    def __init__(self, name, listofmarks):
        self.name=name
        self.listofmarks=listofmarks
        
    # @staticmethod
    # def avg():
           
    def avg(self):
        
        sum=0
        for eachvalue in self.listofmarks:
            sum=sum+eachvalue
    
        avg=sum/3
        print("Average : ",avg)
        
stud1=stud("Rathod",[99,76,85])
print("Name is Student : ",stud1.name)
print("List of Marks student is : ",stud1.listofmarks)
stud1.avg()
