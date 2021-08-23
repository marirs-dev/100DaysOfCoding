import pandas
nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_alphabets_dict = {row.letter: row.code for (index,row) in nato_alphabets.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Please enter word: ").upper()
input_word_list = [letter for letter in input_word]
nato_alphabets_result = [nato_alphabets_dict[letter] for letter in input_word]
print(nato_alphabets_result)
