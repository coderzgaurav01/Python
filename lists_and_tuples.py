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

tup = (10,20,30,40,50)
print(tup)
print(tup[0])

print(tup[1:3])

#Methods in tuple

print(tup.index(20))


#Wap to ask the user to enter names of their 3 favourite movies and store them in a list
movies=[]
mov1=input("Enter first movie:")
mov2=input("Enter second movie:")
mov3=input("Enter third movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


#Wap to check if a list contains palindrome of elements.

list=[1,2,3,3,2,1]
print(list)
list2=list.copy()
print(list2)
list2.reverse()
print(list2)
if(list==list2):
    print("List is palindrome")
else:
    print("List is not palindrome")