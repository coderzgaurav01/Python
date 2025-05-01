#Basic concept
age = int(input("Enter Your age: "))
if(age>18):
    print("You are eligible to drive") 
elif(age>=16 and age<18):
    print("Wait for 2 year bro ")  
else:
    print("You are not eligible bro!!")

    
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
    

# ODD/Even
num = int(input("Enter the number:"))
if(num%2==0):
    print("Even")
else:
    print("Odd")

#Greatest among three

num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter third number: "))

if(num1>num2 and num1>num3):
    print(num1,"Is the greatest number")
elif(num2>num1 and num2>num3):
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")
    

# Multiple of 7
num1=int(input("Enter The number: "))
if(num1%7==0):
    print(num1,"is the multiple of 7")
else:
    print(num1,"is not multiple of 7")
