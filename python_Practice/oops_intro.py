'''Feature of OOps(Object oriented programming system)
1.Class and Objects
2.Encapsulation
3.Abstraction
4.Inheritance
5.Polymorphism
'''
#class and objects
print("--------Class and Objects------")
class Person:
    name = 'Raju'
    age =  20
    def talks(self):
        print(self.name)
        print(self.age)
p1 = Person()
p1.talks()

#Encapsulation
print("----------Encapsulation---------")
"""Encapsulation is nothing but attributes(variables) and methods inside of the class"""
class Student:
    def __init__(self):
        self.id = 10
        self.name = "Raju"
    def display(self):
        print("Id of student",self.id)
        print("name of student",self.name)
s1 = Student()
s1.display()

#Abstraction
print("--------Abstraction-------")
"""Abstraction is nothing but the process to  hide the unneccessary data from users
For this process we have to use double under score or single underscore to discribe the methods or variables in python
"""
class MyClass:
    def __init__(self):
        self.__y = 3 #This is private variable
m = MyClass()
#print(m.y) # its will give the error bcous y is a private variable
print(m._MyClass__y) #For printing the private variable we have to use single underscore before the class
#undestanding public and private variable
class MyClass:
    def __init__(self):
        self.x = 10
        self.__y = 2
    def display(self):
        print(self.x)
        print(self._MyClass__y) #its called name mangling
print("Accessing Variable through method :")
m = MyClass()
m.display()
print("Accessing variable through instance")
print(m.x)
print(m._MyClass__y) #requared name mangling


#Accessing some part of the data
class Bank:
    def __init__(self):
        self.accno = 10
        self.name = 'Srinu'
        self.balance = 5000.00
        self.__loan = 1500000.00
    def display_to_clerk(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        #print(self.loan)
        #print(self._Bank__loan)
b1 = Bank()
b1.display_to_clerk()

#inheritance:-Creating new class from existing class
print("--------Inheritance--------")
class A:
    a = 1
    b = 2
    def method1(self):
        print(self.a)
        print(self.b)

class B(A):
    c = 3
    def method2(self):
        print(self.c)

b1 = B()
#b1.method2()
b1.method1()

#Polymorphism:-Polymorphism represnt the ability to assume several different form
print("-----------Polymorphism---------")
def add(a,b):
    print(a+b)

add(8,2) #add method work for int
add("Mohd"," Shmsad") # same add method work for string {This is called polymorphism}