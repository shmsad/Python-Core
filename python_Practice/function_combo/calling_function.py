#function to add two numbers
def add(a,b):
    """This function find sum two Numbers"""
    c = a+b
    print("Sum of two number is = ",c)
#call the function
add(10,15)
add(1.5, 10.75) #call second time

#returning result from a function
def sum(a,b):
    c = a+b
    return c
x = sum(10,15)
print("The sum of x is :",x)
y = sum(10.23,3.65)
print("The sum of y is: ", y)

# a function to test whether a number is even or odd
def even_odd(num):
    """To know num is even or odd"""
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

even_odd(15)
even_odd(12)