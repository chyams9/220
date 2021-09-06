"""
Name: <ChrisHyams>
interest.py

Problem: This function calculates the monthly interest charge of a credit card.
"""


def Daily_balance():
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    days_in_billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter the previous net balance: "))
    payment_amount = eval(input("Enter the payment amount: "))
    date_of_payment = eval(input("Enter the day of the billing cycle the payment was made: "))
    step_1 = net_balance * days_in_billing_cycle
    step_2 = payment_amount * (days_in_billing_cycle - date_of_payment)
    step_3 = step_1 - step_2
    step_4 = step_3 / days_in_billing_cycle
    step_5 = annual_interest_rate / 12 / 100
    step_6 = step_4 * step_5
    print("Monthly interest charge: ", step_6)

Daily_balance()


