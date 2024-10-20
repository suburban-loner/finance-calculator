import math
# financial calculators for investments and home loan repayments.

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()

# Calculation of investment.
if calculation_type == "investment":
    amount = float(input("Enter the amount of money you are depositing:"))
    interest_rate = float(input("Enter the interest rate(number only) of the investment:"))
    time = float(input("Enter the number of years you plan on investing:"))
    interest = input("Will you be using 'simple' or 'compound' interest:").lower()
    r = interest_rate / 100
    # Calculations of simple and compound interest.
    if interest == 'simple':
        total = amount * (1 + r * time)
    elif interest == 'compound':
        total = amount * math.pow((1 + r), time)
    print("Your total amount will be R" + str(total))

# Calculation of bond.
elif calculation_type == "bond":
    amount = float(input("Enter the present value of the house:"))
    interest_rate = float(input("Enter the interest rate of the bond:"))
    time = float(input("Enter the number of months you plan to take to repay the bond:"))
    interest = interest_rate / 100
    i = interest / 12
    # Calculation of repayment amount
    repayment = (i * amount) / (1 - (1 + i)**(-time))
    print("You will have to repay R" + str(repayment) + " each month.")

# Error message for invalid input
else:
    print("You have entered an invalid input")
