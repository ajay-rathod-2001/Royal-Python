# Function with parameter

# def addition(a,b):
#     print("Addtion : ",a+b)
# addition(10,80)
    

# def getNumber(a,b):
#     return 100,200
# x=getNumber()
# print(x)
    
    
#key Word Arguments
    
# def add(a,b):
#     print(a+b)

# add(b=19,a=10)

# def setCity(city="pune",gender="Male"):
#     print(city,gender)
    
# setCity("Yavatmal","female")


# def total(*numbers):
#     print(numbers)
# total(1,2,3,4)


def total(*numbers):
    print(sum(numbers))
total(1,2,3,4,6)