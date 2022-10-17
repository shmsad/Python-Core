#import math liberaries
import math
x = math.sqrt(16)
print("sqr root of 16 using math.sqrt : ", x)
import math as m
print(m.sqrt(x))
print("we can use one by one as from math import factorial")
from math import sqrt, factorial
x = sqrt(64)
y = factorial(5)
print("factorial of 5  and sqrt of 64")
print("factorial of : ",y,"sqrt of 64 : ", x)
#if we import only math then we have to use math.func
print("math.ceil(4.5) : ",math.ceil(4.5))
#if we import module name using from
from math import ceil
print("ceil(4.4) : ", ceil(4.4))
print("math.floor(6.3) : ", math.floor(6.3))
x = 3.14159
print("let assume x = 3.14159")
print("degrees of x : ", math.degrees(x))
print("radians of x : ", math.radians(x))
print("let assume x = 0.5")
x = 0.5
print("sin of x : ", math.sin(x))
print("cos of x : ", math.cos(x))
print("tan of x : ", math.tan(x))
print("Exponentiation of x : ", math.exp(x))
print("fabs of -4.56 : ", math.fabs(4.56))
print("factorial of 4 : ", math.factorial(4))
print("fmod(x,y) of fmod(4.5, 3) : ", math.fmod(4.5,3))
print("fsum return accurate sum of floating point values : ", math.fsum([1.5,2.4,-3.3]))
print("modf returns float and integer part : ", math.modf(2.56))
print("log10(x) : ", math.log10(5.2345))
print("log(5.5,2) : ", math.log(5.5,2))
print("pow(x,y) : ", math.pow(4,5))
print("gcd=>gratest common devision of given number => gcd(25,30)", math.gcd(25,30))
print("truncate in to int trunc(15.5676) : ", math.trunc(15.5676))
print("isinf => cheack +ve and -ve infinite : ", math.isinf(float("inf")))
print("isnan => cheack nan value : ", math.isnan(float("NaN")))
print("-------constant in math------")
print("Value of PI : ",math.pi)
print("Value of e : ", math.e)
print("Value of inf : ", math.inf)
print("Value of NaN : ", math.nan)
