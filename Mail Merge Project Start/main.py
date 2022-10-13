#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as name_list:
    clean_names = []
    list_of_names = name_list.readlines()

for name in list_of_names:
    stripped_name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as starting_letter:
        letter = starting_letter.read()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)


