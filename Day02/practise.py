# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welcome to Tip calculator.")
bill = float(input("What is the bill?\n$"))
tip_percentage = float(input("What is the tip percentage? \n%"))
num_of_ppl = int(input("How many people are there? \n"))
bill_per_person = (bill/num_of_ppl) * (1 + tip_percentage /100)
# print(f"Each person should pay:{round(total_pay,2)}")
print(f"Each person should pay: ${'{:.2f}'.format(bill_per_person)}")
