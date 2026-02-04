# Dictionary :

stud={
    "name":"Ajay Rathod",
    "age":24,
    "city":"Morchandi",
    "RollNo":476
}

print(type(stud))

print(stud["name"])

print(stud)

stud["city"]="hyd"
print(stud)

stud["favColor"]="Red"
print(stud)

stud.pop("favColor")
print(stud)

print(stud.keys())
print(stud.values())
