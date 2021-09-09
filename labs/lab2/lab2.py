"""
Name: <Chris Hyams>
<lab2>.py

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    acc = 0
    for x in range(0, upper_bound + 1, 3):
        acc = x + acc
    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l,end=" ")
        print()


def triangle_area():
    import math
    a = eval(input("Enter side A: "))
    b = eval(input("Enter side B: "))
    c = eval(input("Enter side C: "))
    s = (a + b + c) / 2
    x = (s * (s - a) * (s - b) * (s - c))
    A = math.sqrt(x)
    print("Area= ", A)


def sum_of_squares():
    lower_range = eval(input("Enter the lower range:"))
    upper_range = eval(input("Enter the upper range:"))
    acc = 0
    for x in range(lower_range, upper_range + 1):
        acc = (x * x) + acc
    print(acc)


def power():
    base = eval(input("Enter the base:"))
    exponent = eval(input("Enter the exponent:"))
    acc = 1
    for x in range(exponent):
        acc = acc * base
    print(base, "^", exponent, "=", acc)


