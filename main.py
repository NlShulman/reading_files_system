
with open("./Input/Letters/starting_letter.txt") as l:
    letter = l.read()

with open("./Input/Names/invited_names.txt") as n:
    names = n.read().splitlines()

for name in names:
    with open(f"./Input/Letters/letter_for_{name}.txt", mode="a") as file:
        file.write(letter.replace("[name]", name))

