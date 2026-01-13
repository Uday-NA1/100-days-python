with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

for name in names:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt") as starting:
        contents = starting.read()
        letter = contents.replace("[name]", name)

        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as final:
            final.write(letter)