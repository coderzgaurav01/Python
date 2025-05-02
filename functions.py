
def sum(a,b):
    return a+b
c=int(input("Enter number1 : "))
d=int(input("Enter number2 : "))
print(sum(c,d))

#WAF to print the length of the list.
num=[1,2,3,4,5]
def len_of_list(list):
    print(len(list))
len_of_list(num)

#waf to print the elements of a list in a single line
def list_in_one_line():
    list=[1,2,3,4,5]
    for i in list:
        print(i,end=" ")
list_in_one_line()


#Waf to find the factorial of n
def factorial(n):
    fact=1
    if(n==0 or n==1):
        print(1)
    else:
        for i in range(1,n+1):
            fact=fact*i
    print(fact)

factorial(0)


def odd_even(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
        
odd_even(6)


#recursion
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    
show(5)

def factorial(n):
    if(n == 0):
        return 1 
    return n * factorial(n - 1)

print(factorial(5))
a=int(input("Enter the number:"))
result=factorial(a)
print(result)

def nat_num(n):
    if(n == 0):
        return 0
    return nat_num(n - 1)+n

sum = nat_num(5)
print(sum)


