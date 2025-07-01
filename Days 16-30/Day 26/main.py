import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabet_data.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word_to_convert = input("Enter a word: ").upper()
    try:
        converted_word = [phonetic_dict[letter] for letter in word_to_convert]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(converted_word)

generate_phonetic()
