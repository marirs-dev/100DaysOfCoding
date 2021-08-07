# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percent of tip would you like to give? 10, 12 and 15? "))
split_count = int(input("How many people to split the bill? "))
total_pay = (total_bill / split_count) * (1+tip_percentage/100)

# print(f"Each person should pay:{round(total_pay,2)}")
print(f"Each person should pay: ${'{:.2f}'.format(total_pay)}")
