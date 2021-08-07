import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if 3 > choice >= 0:
    print(game_image[choice])
    print("Computer choice:")
    print(game_image[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice == 2:
        print("You lose!")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You win!")
    elif computer_choice == choice:
        print("It's a draw")
else:
    print("You types an invalid number, you lose!")

