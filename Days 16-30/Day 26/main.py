import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word_to_convert = input("Enter a word: ").upper()
converted_word = [phonetic_dict[letter] for letter in word_to_convert]
print(converted_word)
