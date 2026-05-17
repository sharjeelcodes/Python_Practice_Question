intro={
    "name":"Sharjeel",
    
    "age" : 19,
    "cast":"jutt",
    "subject":["English","Urdu","Math","Programming fundamentals"],
    "numbers":(461, 878,361,773),
    
}
print(intro["name"])
print(intro["subject"])
intro["cast"]="bharoka jutt"
intro["surname"]="Muhammad"
print(intro)
null_dic={
    
}
null_dic["name"]="muhammadsharjeel"
print(null_dic)

student={"name":"sharjeel",
         "department":"computer science",
        "subjects": {"chm":73,
                     "phy":65,
                     "math":73,
                     "urdu":85,
                     "english":85 },
        "learning":"phython",
    
}


print(student)
print(student["subjects"])
print(student.keys())
print(len(student["subjects"]))
print(tuple(student))
print(list(student))
print(str(student))
print(student.values())
print(len(student))
student["name"]="Ali raza"
print(student)
print(student.items())
print(len(student))
print(student.get("name"))  
print(student.get("names"))
new_dic={"name":"kashif","age":"16"}
student.update(new_dic)
print(student)



mydic={
    "name":"Sharjeel",
    "age":19,
    "marks":773,
    "langaguge":"python",
    "subjects":["English","70","Urdu","80","Math","75"],
    "learning":("python","C++","C","Java","Javascript"),
   
}
print(mydic)
 
##SETS
collection={1,2,3,4,"hello","sharjeel","learning","python",5,6,3,3,2}
print(collection)
print(type(collection))
print(len(collection))
sets=set()
sets.add(1)
sets.add(2)
sets.add("coding")
sets.add((1,2,3,44))
sets.remove("coding")
sets.pop()
sets.pop()
print(sets) 
set1={1,2,3,4,5}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))




 