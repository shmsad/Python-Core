x = True
print("value of x :", x)
x = False
print("Value x is :", x)

#Logical gate ===> and or not

# OR operator
# Coffee or tea
print("OR 1 :", True or False) # True
print("OR 2 :", True or True) # True
print("OR 3 :", False or True) # True
print("OR 4 :", False or False) #False

#AND Operator
#Guest Water and Coffee
print("AND 1 :", True and False) # False
print("AND 2 :", False and True) # False
print("AND 3 :", False and False) # False
print("AND 4 :", True and True) # True

'''
Condition1 AND/OR condition2 AND/OR condition3
not condition
'''
print("Cond 1 :", 12>15 and 15<13) # False and False =>False
print("Cond 2 :", 12>10 and 4<12) # True and True => True
print("Cond 3 :", 12>8 and 52<45) # True and False => False