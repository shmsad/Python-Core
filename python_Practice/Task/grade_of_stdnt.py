#Find Grade of stident based on below requirement
#mark >= 80 => A+, 60-79 => A, 50-60 => B, 40-50 => C, Below 35 Fail
#1.STATE - recieve user input
marks = int(input("Enter Student Mark"))
if marks >= 0 and marks <= 100:
    print("Valid marks")
    if marks >= 35:
        print("Result : Pass")
        if marks >= 80:
            print("Grade : A+")
        elif marks < 80 and marks >= 60:
            print("Grade : A")
        elif marks < 60 and marks >= 50:
            print("Grade : B")
        elif marks < 50 and marks >= 40:
            print("Grade : C")
    else:
        print("Result : Fail")
else:
    print("Invalid marks")
