# a function to check whether number is prime or not
def prime(num):
    """check if num is prime or not"""
    x = 1 #this will be zero if not prime
    for i in range(2, num): #devide n from 2 to n-1
        if num%i == 0: #if devisible by any number
            x = 0 #take x as 0
            break
        else:
            x = 1 # else x take as 1
            return x
# test if a number is prime or not
num = int(input("Enter a number: "))
#check number is prime or not
result = prime(num)
if result == 1:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


def prime(num):
    """to check if n is prime or not"""
    x = 1 # this will be zero if not prime
    for i in range(2, num):
        if num%i == 0:
            x = 0
            break
        else:
            x = 1
    return x
"""num = int(input("Enter number"))
result = prime(num)
if result == 1:
    print(num,"is prime")
else:
    print(num, "is not prime")
"""
num = int(input("How many prime number do you want: "))
result = prime(num)
#print(result)
i = 2
c = 1
while True:
    if prime(i): # if i is prime dusplay it
        print(i)
        c+=1
    i+=1
    if c>num:
        break