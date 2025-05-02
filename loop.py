'''
i=0
while (i<=5):
    print(i)
    i=i+1

for i in range(5):
    print(i)
   
#Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1

#print numbers from 100 to 1
i=100
while(i>=1):
    print(i)
    i=i-1
    

n=int(input("Enter the number of n: "))
i=1
while i<=10:
    print(n*i)
    i=i+1

list=[]
i=1
while i<=10:
    a=i*i
    list.append(a)
    i=i+1
    
print(list)
print(len(list))
x=int(input("Enter element want to search"))
i=0
while(i<len(list)):
    if(x==list[i]):
        print(x," present at index ",i)
        break
    i=i+1
    if(i==len(list)):
        print("element not present in list")    


#for loops are used for sequential traversal. FOr traversing list string tuples
list=[1,2,3]
for el in list:
    print(el)
    
str="Prince kumar"
for char in str:
    print(char)
    
for el in range(1,10,2):
    print(el)

for i in range(100,0,-1):
    print(i)  

#wap to find the sum of first n numbers
n=int(input("Enter the value of n: "))
i=0
sum=0
while(i<=n):
   sum=sum+i
   i=i+1

print("Sum of ",n,"number is: ",sum)
    
'''
n=int(input("Enter the number: "))
fact=1
   
for i in range(1,n+1):
    if(n==0 or n==1):
        print(n)
    else:
      fact=i*fact 
print("factorial is: ",fact) 
    