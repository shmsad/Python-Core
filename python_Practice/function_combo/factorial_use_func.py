# a function to calculate factorial value
"""def fact(n):
    """"to factorial value""""
    prod = 1
    while n >= 1:
        prod*=n
        n-=1
    return prod

for i in range(1,11):
    print("Factorial of {} is {}".format(i,fact(i)))"""
def fact(num):
    """This function is a factorial function"""
    prod = 1
    while num>=1:
        prod*=num
        num-=1
    return prod
for i in range(1,10):
    print("factorial of {} is {} ".format(i,fact(i)))