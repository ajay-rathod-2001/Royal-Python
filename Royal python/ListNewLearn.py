fruits=["apple","orange","cherry","apple"]
print(fruits)

# creates List in Python :

colors=["red","green","blue"]
print(colors)

numbers=[1,2,3,4]
print(numbers)

mixed=[1,"Ajay",3.14,True]
print(mixed)

nested=[1,[2,3],[4,5,6]]
print(nested)

print(fruits[0])
print(colors[2])
print(mixed[2])
print(fruits[-1])

# Changing an Elements:

fruits[1]="blueberry"
print(fruits)

fruits.append("mango")
print(fruits)

fruits.remove("cherry")
print(fruits)

# Joint Lists:

list1=[1,2]
list2=["a","b"]

list3=list1 + list2
print(list3)

# Using Appen Methods:

for x in list2:
    list1.append(x)
    print(list1)
    
list1.extend(list2)
print(list1)

print("\n")
# List Comprehensions :
print("list of Comprehensions : ")

sqr=[x**2 for x in range(1,6)]
print(sqr)

evn_num=[x for x in range(1,11) if x%2==0 ]
print(evn_num)

fruits=["Apple","Banana","Cherry"]
uppercase_fruits=[fruit.upper() for fruit in fruits]
print(uppercase_fruits)

print("\n")

# Flatten A List :

def flattenlist(lst):
    return[ item for sublist in lst for item in sublist]

nestedlist=[[1,2],[3,4],[5,6]]
flattened=flattenlist(nestedlist)
print(flattened)

# Iterative Over Lists :

print("\n","Iterative Over list : ")

for fruit in fruits:
    print(fruit)
    
index =0

while index < len(fruits):
    print(fruits[index])
    index+=1





