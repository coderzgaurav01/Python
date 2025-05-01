"""
age = int(input("Enter Your age: "))
if(age>18):
    print("You are eligible to drive") 
elif(age>=16 and age<18):
    print("Wait for 2 year bro ")  
else:
    print("You are not eligible bro!!")
"""
    
#Grading system
name = input("Enter Your Name : ")
print("Welcome in the world of education Mr.",name)
print("You are here to know your grade based on your marks")
marks = int(input("Enter the marks :"))
if(marks>=90):
    print("Grade A")
elif(marks<90 and marks>=80):
    print("Grade B")
elif(marks<80 and marks>=70):
    print("Grade C")
else:
    print("Grade D")