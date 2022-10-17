#addition
print("Int: Addition of numbers")
print("----Approach 1----")
print(10+20) # Hard coding single time using
print("----Approach 2----")
#lets assume x = 10
x = 10
y = 20 # multiple time use
print(x+y)
print("further bussines logic")
print(x*x + y*y)
print("-----Approach 3.1------")
x = 10
y = 20 # static way of initialization
print("Addition is :", x+y) # one time usage
print("sum of sqr :", x*x + y*y)
print("---Approach 3.2-----")
x = int(input("Enter Number1 :"))
y = int(input("Enter Number2 :"))
output = x+y
print("Addition is :", output)
print("further bussines logic", x+y+output)

#Different use cases/scenarios
print("-------Both negative number-------- ")
x = -23
y = -56
res = x + y
print("Addition of number :", res)

print("----negative and positive number----")
x = -78
y = 54
res = x+y
print("Addition of number :", res)

print("------Positive and negative-----")
x = 78
y = -36
res = x+y
print("Addition of number :", res)

print("------Positive and zero-----")
x = 45
y = 0
output = x+y
print("Addition of number :", output)
#Addition of three numbers
x = 10
y = 35
z = 45
res = x+y+z
print("Addition is :", res)

x = -12
y = -65
z = -23
res = x+y+z
print("Addition is :", res)

#Every mathemetical Calculation
print("Fraction values", 3/7+6/5) #BODMAS <==> Operator Precedence
#int + float
print("---Int+float----")
x = 12
y = 15.63
res = x+y
print("Addition is :", res)

print("----float+int")
x = 18.326
y = 52
res = x+y
print("Addition is :", res)

print("----complex+int------")
x = complex(2+3)
y = 45
res = x+y
print("Addition is :", res)

print("---complex+float-----")
x = complex(5+6)
y = 25.36
res = x+y
print("Addition is :", res)

print("----int+complex-------")
x = 15
y = complex(5+78)
res = x+y
print("Addition is :", res)
print("----float+complex------")
x = 12.36
y = complex(45+63)
res = x+y
print("Addition is :", res)

