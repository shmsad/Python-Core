"""#cheack if a list consist any aliment or not
a = ['python','java','rlang','golang','b','sql','java','python','python','rlang','sql','java']
#check either list empty or not
#if empty print no element in list
#if have cheack psql is present or not
# if present then print if not then print
#python , java present or not
#present print if not then also print
#count of java
#count each repeted element , element as key and occurence as a value
d1 = {}
if len(a)>0:
    print("list is not empty")
    for i in a:
        if 'psql' in :
            print("psql is present")
        else:
            print("psql is not present")
            break
    for i in a:
        #if i=='python' or i == 'java':
        if "python" in a and 'java' in a:
            print("java and present")
            print("java=>",a.count('java'))
            print("python=>",a.count('python'))
        else:
            print("not present")
        break
else:
    print("No element in list")

d1 = {}"""
a=['python','java','rlang','golang','rubby','sql','java','python','rlang','sql','java']
'''
either having element,
if empty print no elements,
if data check psql present or not,print p sql is present else,
if bot python java present
count of java
each element count
print values in list
'''
if len(a)!=0:
    print('List has elements')
    if 'psql' in a:
        print('psql is present')
    else:
        print('psql not present')
    if 'python' in a and 'java' in a:
        print('Python and java both present')
        print('count of java=',a.count('java'))
        d={}
        b=set(a)
        for i in b:
            c=a.count(i)
            d[i]=c
        print(d)
        for j in d.items():
            print(j)

    else:
        print('Java and python not present')
else:
    print('List is empty')