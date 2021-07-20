# Day 1 of "100 Days Of Code"

Today I have revised below concepts in Python:  
* Printing to the Console in Python
* String Manipulation
* Python Input function
* Python variables
* Variable Naming

Day 1 Project:
I have implemented the following steps:
1. Greeting message
2. Ask a question "What's the name of city you grew up in?"
3. Take input from user
4. Ask a question "What is the name of your pet?"
5. Take input from user
6. Print the band name by concatenating city name and pet name.

```buildoutcfg
# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
# 2. Ask the user for the city that they grew up in.
city = input("What's the name of city you grew up in?\n")
# 3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name.
print(f"Your band name could be {city} {pet}")
# 5. Make sure the input cursor shows on a new line.

```
Output:
```buildoutcfg
Welcome to the Band Name Generator.
What's name of the city you grew up in?
Vizag
What is the name of your pet?
Leo
Your band name could be Vizag Leo

```