import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
on = True
while on:
    user_input = input("Enter a word: ").upper()
    try:
        new_list = [new_dict[code] for code in user_input]
    except KeyError:
        print("sorry,please enter just a number ")
    else:
        print(new_list)
        break
