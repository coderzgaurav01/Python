#class
#class is the blueprint for creating object
class student:
    def __init__(self,name):
        self.name=name
        
    @staticmethod #decorator
    def hello():
        print("hello")
    
s1 =student("Gaurav")
s2 = student("Ajay")
print(s1.name)
print(s1.hello())
print(s2.name)