#Dictionaries are used to store data values in key:value pairs

student={
    "Name":"Gaurav Pathak",
    "Education": "Btech Cse AI&ML",
    "CGPA":8.7,
    "Role":["Python Developer","ML engineer","AI researcher","Mern Stack developer"],
    "Salary":1200000
    
}
print(student)
print(type(student))
print(student["Name"])
print(student["CGPA"])

player={
    "Name": "Ms Dhoni",
    "Age":43,
    "Profession":"Wicket-keeper Batsman",
    "Score":{
        "Test":10000,
        "ODI":11000,
        "T20":15000
    },
    "Achievement":("World Cup ODI","T20 world cup","Championstrophy","Ipl trophy")
}

print(player)
print(player["Score"])
print(player["Score"]["ODI"])
print(player.keys())
print(player.values())
print(player.items())
pairs=list(player.items())
print(pairs[0])
print(player.get("Name"))
player.update({"City" : "Ranchi"})
print(player.get("City"))
print(player)


#set is the collection of unordered items
nums={1,2,3,4}
print(nums)

set2={1,2,2,3,3,4,1,2}
print(set2)
print(len(set2))

set1={5,6,7,8}
print(set2.union(set1))
print(set2.intersection(set1))

null_set=set()
print(null_set)

set2.add(5)
print(set2)

#set2.add([1,2,3,4])
#print(set2)
#we cannot add list or disctionaries to the set as their elements are mutable but sets elements are immutable

set2.remove(5)
print(set2)

set1.clear()
print(set1)

set2.pop()
print(set2)

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary &add one by one . Use sublect name as key&marks as values
marks={}
a=int(input("Enter the marks of phy"))
b=int(input("Enter the marks of biology"))
c=int(input("Enter the marks of maths"))

marks.update({"Phy":a,"Bio":b,"Math":c})
print(marks)

set1={
     ("float",9.0),
      ("int",9)
    }
print(set1)