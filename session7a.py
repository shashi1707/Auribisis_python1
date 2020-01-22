""">>>>>>>>>>>>>>>>>>>LIST<<<<<<<<<<<<<<<<<<<<<<<<<<<"""

students=['john','jennie',"jim",'jack','joe']
print(students)
print(type(students))

#1.concatination>>>>can only concatenate list not "tuple" OR ANY OTHER DATASTRUCTURE to list
print(students+['fionna',"george"])
newstudents=students+['fionna',"george"]
print(students)
print(newstudents)
#2.Repetion
print(students*2)
#3.Membership
print('john' in students)
print("dave" not in students)

#4 Indexing
print(students[0])
print(students[len(students)-1])


#5.Slicing
print(students[0:2])
print(students[1:4])
filteredstudents=students[1:4]

for i in range(0,len(students)):

    print(students[i])
print("*********************")

#EXTENDED VERSION OF FOR:
for student in students:
    print(student)
