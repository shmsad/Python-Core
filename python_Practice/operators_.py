#Arithmetic operator
a = 13
b = 5
print("Put The value a = ", a,"and b = ", b)
print("---Addition---")
res = a+b
print("Addition of number :", res)
print("----Substraction-----")
res = a-b
print("Subtraction of number is :",res)
print("----Multiplication----")
res = a*b
print("Multiplication of number is :", res)
print("-----Division-----")
res = a/b
print("Division of Number is :", res)
print("----Floor Divison -----")
#Integer Devison
res = a//b
print("Floor Division of number is :", res)
print("----Modulus----")
#Gives remainder of devision
res = a%b
print("Modulus of number is :",res)
print("---Exponent-----")
#power:-in this a to the power of b
res = a**b
print("Exponent of number is :",res)


#Precendency of the operators
print("If we have value x =1,y = 2, z= 3, a = 2, b = 2, c = 3 "
      "and equation d = (x*y)*z**a//b+c then output based of operator precedency")
x = 1
y = 2
z = 3
a = 2
b = 2
c = 3
res = (x+y)*z**a//b+c
print("result of the given expresion",res)

#Assignment Operators
#let us assume x = 20 and y = 10 and z = 5
x = 20
y = 10
z = 5
print("value x is :",x, "Value of y is :",y, "Value of z is :",z)
z = x+y
print("Addition of z = x+y is : ", z)
z+=x
print("z+=x is : ", z)
z-=x
print("z-=x is : ", z)
z*=x
print("z*=x is : ", z)
z/=x
print("z/=x is : ", z)
z//=x
print("z//=x is : ", z)
z%=x
print("z%=x is : ", z)
z**=x
print("z**=x is : ", z)

print("a=b=1")
a=b=1
print("a : ",a,"b : ", b)

print("Unary Minus using value n = 10")
n = 10
print("-n = ", -n)
print("use num = -10 and change it into num = -num")
num = -10
num = -num
print("num = ", num)

#Relational Operators
print("Relational operator a = 1 and b = 2")
a = 1; b = 2
print("a>b : ", a>b)
print("a>=b : ", a>=b)
print("a<=b : ", a<=b)
print("a==b : ", a==b)
print("a!=b : ", a!=b)

if (a>b):
      print("YES")
else:
      print("NO")

print("put x = 10 and use 10<x<20 ")
x = 15
print("Result : ", 10<x<20)
print("use 10>=x<20 Rsult : ", 10>=x<20)
print("Use 10<x>20 Result : ", 10<x>20)

#Logical Operators
print("----Logical Operators-----")
print("Assume x = 1 and y = 2")
print("x and y is : ", x and y)
print("x or y is : ", x or y)
print("Not x", not x)

#Boolean Operators
print("-----Boolean Operators------")
print("Assume x = True and y = Fales")
x = True; y = False
print("x and y => ", x and y)
print("x or y => ", x or y)
print("not x => ", not x)

#Bitwise operators
print("----bitwise----")
print("let assume x = 10 and y = 11")
x = 10
y = 11
print("complement of x to ~x : ", ~x)
print("x AND y : ", x & y)

#Membersship Operator
print("-----membership------")
names = ["Rani","Yamini","Sushmita","Veena"]
for name in names:
      print(name)

postal = {"postal":110001, "Chennai":600001, "Kolkata":700001, "Bangaluru":560001}
for city in postal:
      print(city," and ",postal[city])


print("Rani" in names)
print("Rakesh" not in names)
print("Sushmita" not in names)
print("postal" in postal)

#Identity
print("---Identity----")
a = 25
b = 25
print("id(a) and id(b) if a = 25 and b = 25 => ", id(a), id(b))
print("a is b : ", a is b)
print("a is not b : ", a is not b)
print("id(a) is id(b) : ", id(a) is id(b))
print("id(a) is not id(b) : ", id(a) is not id(b))
print(id(2519976930352))
print(id(2519976930352))
