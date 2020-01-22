"""Sequences in Python
    Sequence : Data with quite similar type
    Sequences listed below is also known as
    Built In Data Structures here in Python
    Why Data should be Structured?
    1. Sort
    2. Search
    3. Filter
    PS: Must be done in least possible time !!
    1. Tuple
    2. List
    3. String
    3. Set
    4. Dictionary
    Operations on Sequences:
    1. Concatenation
    2. Repetition
    3. Membership Testing
    4. Slicing
    5. Indexing
"""
>>>>>>>>>>>>>>TUPLE<<<<<<<<<<<<<<,

students = ('john', 'jennie', "jim", 'jack', 'joe')
print(students)
print(type(students))
#1.Concatination>>>ONLY CONCATINATE THE TUPLE NOT ANY OTHER I.E LIST OR SET OR DICTIONARY
print(students+('fionna', "george"))
#2.Repetion
print(students*2)
#3.Membership>>>USED TO CHECK THE MEMBER PRESENT IN TUPLE OR NOT
print('john' in students)
print("dave" not in students)

#4 Indexing>>>>>STARTING FROM 0
print(students[0])
print(students[len(students)-1])


#5.Slicing>>>>[X,Y]>>>MEANS X INCLUSIVE AND Y EXCLUSIVE
print(students[0:2])
print(students[1:4])
filteredstudents=students[1:4]

for i in range(0,len(students)):
    print(students[i])
print('<<<<<<>>>>>>>><<<<>>>')

#Extended version of for:
for student in students:
    print(student)
