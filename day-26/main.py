import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet)

def translate():
    word = input("Enter a word: ").upper()
    try:
        result = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        translate()
    else:
        print(result)


translate()
