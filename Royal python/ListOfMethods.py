# Mehtods in List :

# Indexing :

marks=[99,100,79,95]
print(marks)

marks[2]=85
print(marks)

# Slicing :

print(marks[1:4])
print(marks[:2])

print(max(marks))
print(min(marks))

marks.append(90)
print(marks)

marks.sort()
print(marks)

marks.pop(3)
print(marks)

marks.remove(95)
print(marks)

marks.insert(2,95)
print(marks)

# Practice :

# take three food And Storde in list, print list and lenght of list

food=input("Enter Food 1: ")
food1=input("Enter Food 2 : ")
food2=input("Enter Food 3: ")

# foodList=[food,food1,food2]
# print(len(foodList))

foodList=[]

foodList.append(food)
foodList.append(food1)
foodList.append(food2)

print(foodList)
print(len(foodList))
