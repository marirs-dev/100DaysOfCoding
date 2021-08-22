PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.read().split("\n")

for name in names_list:
    stripped_name = name.strip()
    new_letter = letter_text.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", mode="w") as save:
        save.write(new_letter)
