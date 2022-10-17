"""#to accept more than one input in the same line
a,b = [int(x) for x in input("Enter two nmubers use space while enter: ").split()]
print("Devision of {0} and {1} is = {2}".format(a,b, a/b))

var1, var2, var3 = [int(x) for x in input("Enter Three number while enter use comma: ").split(',')]
print("prodcut of {0} , {1} and {2} is = {3}".format(var1,var2,var3,var1*var2*var3))

a, b, c, d = [int(x) for x in input("Enter four number only")]
print("The u have entered: ",a,b,c,d)


#Accept group of string from keybord
lst = [x for x in input("Enter name age and address use coma while enter").split(",")]
print("You Entered: ", lst)
"""

"""#Use of eval() Function
a, b = 5,6
print(eval("a+b-4"))
a,b,c = [int(x) for x in input("Enter three numbers for sqr seprate with comma").split(",")]
print(eval("a**b+c"))

#Evaluating an expresion entered from keyboard
x = eval(input("Enter an expresion: "))
print("Result= %d" % x)"""
#Accepting list by input
lst = eval(input("Enter a list: "))
print("List =", lst)

#Acceptinng tuple
tpl = eval(input("Enter a Tuple: "))
print("Tuple =",tpl)

dct = eval(input("Enter Dictionary: "))
print("Dict= ",dct)