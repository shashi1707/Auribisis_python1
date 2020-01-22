#>>>>>>>>>>>>>>>>>>> SET:In set data will be unordered due to Hashing
#                           Data will be UNIQUE
# <<<<<<<<<<<<<<<<<<<<<<<<<

students={'john','jennie',"jim",'jack','jim','joe'}
print(students)#>>>>>>>>>>>>>SET ALWAYS RETURN THE UNIQUE MEMBER IF PRGRAMMER DEFINES THE SAME MEMBER IN SET
print(type(students))

#1.concatination>>>CAN'T BE PERFORMED IN SET DATATYPES
#print(students+('fionna',"george"))
#newstudents=students+{'fionna',"george"}
#print(students)
#print(newstudents)

#2.Repetion>>CAN'T BE PERFORMED IN SET DATATYPES
#print(students*2)

#3.Membership
print('john'  in students)
print("dave" not in students)

#4 Indexing>>CAN'T BE PERFORMED IN SET DATATYPES BECAUSE SET DATATYPE REPRESENTS THE MEMBER IN UNORDERED i.e IN HASHCODE MANNER
#print(students[0])
#print(students[len(students)-1])


#5.Slicing>>>>CAN'T BE PERFORMED IN SET DATATYPES BECAUSE SET DATATYPE REPRESENTS THE MEMBER IN UNORDERED i.e IN HASHCODE MANNER
#print(students[0:2])
#print(students[1:4])
#filteredstudents=students[1:4]

#for i in range(0,len(students)):CAN'T BE PERFORMED IN SET DATATYPES BECAUSE SET DATATYPE REPRESENTS THE MEMBER IN UNORDERED i.e IN HASHCODE MANNER

    #print(students[i])
#enhanced version of for loop
for student in students:
    print(student)
