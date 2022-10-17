#find the maximum number implement using if else logic
"""a = 30
b = 10
c = 20"""
a, b, c = [int(x) for x in input("Enter Three Numbers use comma ").split(",")]
if a > b and a > c:
    print(a, "is largest in numbers")
elif b > c and b > a:
    print(b,"is largest in numbers")
else:
    print(c,"is largest in numbers")