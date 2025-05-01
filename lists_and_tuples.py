# List is a built-in data type that store set of values
marks=[94.4,56.6,95.2,66.4]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])

#list store value of various datatype
student=["Ajay",99,20,"Giridih"]
print(student)

#List slicing
print(marks[1:4])
print(marks[-3:-1])

#List methods
    #append() it's append at the end of list
marks.append(99.2)
print(marks)
    #sort() it sort the list
marks.sort()
print(marks)

#reverse() it reverse the list
marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

#insert() it add elemnt at particular position
marks.insert(3,78.8)
print(marks)

#Tuples
#A built in data type that let us create immutable sequence of values
 