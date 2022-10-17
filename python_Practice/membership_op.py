#membership operator in, not in
#Datatypes : int, float, boolean :: Can't cheack membership
#DataStructure : Membership : String, List, Tuple, Dictionary, Set
str1 = 'Hello World'
list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
dict1 = {1:1, 2:2, 3:3}
set1 = {1, 2, 3, 4, 5, 6}

#in not in
print("L" in str1)
print("l" in str1)
print("d" not in str1)
print(5 in list1)
print(6 in set1)
print(10 in set1)
print(6 not in set1)
print(3 not in tuple1)
import copy
list1  = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6] # shallow copy and deep copy
list2 = list1
list2 = list1.copy() # list1.deepcopy()
print(list1 == list2, id(list1), id(list2))
print(list1 is list2, id(list1), id(list2))

x = 0
print(bool(x))
x = -10
print(bool(x))
print(bool(5))
res = 10-10
print(bool(res))

str1 = ''
print("bool string", bool(str1))
sal = None
print("Val   ", sal, bool(sal))

str1 = 'hello'
print('bool string', bool(str1))
val = [1, 2, 3]
print("value", val, bool(val))