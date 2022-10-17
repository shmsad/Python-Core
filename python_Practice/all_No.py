print("Between 1 to 100")
print("Print all numbers")
x = [x for x in range(1,101)]
print(x)
##for i in range(1,101):
##    print(i)
print("==================")
print("Even Numbers")
x = [x for x in range(1,101) if x%2==0]
print(x)
print("==================")
print("Print Odd Number")
x = [x for x in range(1,101) if x%2 != 0]
print(x)
print("==================")
print("Prime Number")
x = [x for x in range(2, 101)
     if all(x % y != 0 for y in range(2, x))]
print(x)
print("==================")
print("Print numbers with power of 2 (1 2 4 8 16 32 64)")
# enter the length of sequence
##n = int(input("Enter the length of Series: "))
##
##sequence=1
##
##while(n):
##    print(sequence, end =" ")
##    sequence*=2
##    n-=1
n = 100
seq = 1
while(n):
    print(seq,end = " ")
    seq*=2
    n-=1
##x = [x for x in range(1,101)]
 #print(x)
