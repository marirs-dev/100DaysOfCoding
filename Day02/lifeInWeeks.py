# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_left = int(age)
days_left = 365 * (90 - years_left)
weeks_left = 52 * (90 - years_left)
months_left = 12 * (90 - years_left)
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")
