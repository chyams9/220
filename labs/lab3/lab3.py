"""
Name: Chris Hyams
lab3.py
"""

def average():
    number_of_grades = (eval(input("Enter the number of grades: ")))
    acc = 0
    for x in range(0,number_of_grades):
        grade = eval(input("Enter your grade on HW " + str(x + 1)))
        acc = acc + grade
    print(acc / number_of_grades)

def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("Enter your donation amount: "))
    print(acc / donation)


def newton():
    x = eval(input("Enter x: "))
    approx = eval(input("Enter the amount


