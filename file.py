'''
f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
f=open("demo.txt","a")
f.write("\nHi I am gaurav ")
f.close()

f=open("sample.txt","a")
f.write("Hello Everyone")
f.close()
f=open("sample.txt","r")
data1=f.read()
print(data1)
f.close()

import os
os.remove("sample.txt")
'''
with open("practice.txt","w") as f:
    f.write("Hi everyone")
    f.write("\n We are learning I/O")
    f.write("\nusing Python")
    f.write("\nI like programming in Python")
  
with open("practice.txt","r") as f:
    data=f.read()
    
new_data=data.replace("Python","C++")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)