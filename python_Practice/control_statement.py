#If statement
"""x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x==0:
    print("zero")
elif x==1:
    print("single")
else:
    print("more")"""

#for statements
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#create a sample collection
users = {
    'Hans': 'active',
    'Eleonore': 'inactive',
    'ruchi': 'active'
}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

#Strategy : Create a new collection
active_users = {}
for user, status in users.items():
    if status=='active':
        active_users[user] = status


print(active_users)
for i in range(5):
    print(i)
print(list(range(5, 10)))
print(list(range(0,10,3)))
print(list(range(-10,-100,-30)))
a = ['marry','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])


print(range(10))
print(sum(range(5)))
#Break and continue statement
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n, 'equals', x, '*',n//x)
            break
    else:
        print(n, 'is a prime number')