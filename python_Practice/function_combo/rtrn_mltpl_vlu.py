#a function That return two result
def sum_sub(a,b):
    """this function return result of addition and substraction"""
    c = a+b
    d = a-b
    return c, d
#get the result from the sum_sub() function
x, y = sum_sub(10,5)
#display the result
print("Addition of number is: ", x)
print("Substraction of number is: ", y)


# a function that return multiple result
def add_sub_mul_div(a,b):
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    return c,d,e,f
t = add_sub_mul_div(10,5)
#display the result using for loop
print("The result are: ")
for i in t:
    print(i, end=' ')


def display(str):
    return 'hello '+str

#assign a fuunction to a variable
x = display("Ruchi")
print(x)
