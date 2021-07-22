# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_name = name1.lower() + name2.lower()

true_count = total_name.count("t") + total_name.count("r")+total_name.count("u")+total_name.count("e")
love_count = total_name.count("l") + total_name.count("o")+total_name.count("v")+total_name.count("e")

total_score = true_count * 10 + love_count

if total_score < 10 or total_score > 90:
    print(f"Your love score is {total_score}, you go together like coke and mentos.")
elif total_score <= 50 or total_score >= 40:
    print(f"Your love score is {total_score}, you are alright together.")
else:
    print(f"Your love score is {total_score}")
