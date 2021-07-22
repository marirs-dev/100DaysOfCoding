# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if size == "s":
    total_prise = 15
elif size == "m":
    total_prise = 20
elif size == "l":
    total_prise = 25

if add_pepperoni == "y":
    if size == "s":
        total_prise += 2
    else:
        total_prise += 3

if extra_cheese == "y":
    total_prise += 1

print(f"Your final bill is: ${total_prise}")
