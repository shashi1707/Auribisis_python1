students=['john','jennie',"jim",'jack','joe']
print(students,hex(id(students)))

newstudents=students+['fionna',"george"]

students=students+['fionna',"george"]


print(newstudents,hex(id(newstudents)))

print(students,hex(id(students)))

