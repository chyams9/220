"""
Name: <ChrisHyams>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots_made = eval(input("Enter shots made: "))
    total_shots = eval(input("total shots: "))
    percentage = shots_made / total_shots * 100
    print("Shooting Percentage =", percentage)


def coffee():
    pounds_of_coffee = eval(input("Enter pounds of coffee purchased: "))
    shipping_per_pound = 0.86
    fixed_cost = 1.50
    cost_per_pound = 10.50
    Cost_of_shipping = pounds_of_coffee * cost_per_pound + pounds_of_coffee * shipping_per_pound + fixed_cost
    print("Cost of Shipping =", Cost_of_shipping)



def Kilometers_to_miles():
    Kilometers_driven = eval(input("Enter Kilometers Driven: "))
    Miles_driven = Kilometers_driven / 1.61
    print("Mikes Driven=", Miles_driven)


