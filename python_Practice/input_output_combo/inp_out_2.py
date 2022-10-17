#find sum of two number
x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
print("Sum of {0} and {1} = {2}".format(x,y,x+y))

#product of two number
x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
print("Product of {0} and {1} is = {2}".format(x,y,x*y))

#convert number to decimal from any number system
x = input("Enter hexadecimal number: ")
n = int(x, 16)
print("Number hexadecimal to decimal: ", n)

n = int(input("Enter Octal number: "), 8)
print("Octal to decimal: ", n)

n = int(input("Enter binary number: "), 2)
print("Binary to decimal: ",n)