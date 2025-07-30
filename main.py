import random
from constants import *

def main():
    word_list = get_strings(WORD_LIST)
    sp_char = get_strings(CHAR_LIST)

    password = assemble_pw(word_list, sp_char, PASSWORD_LENGTH)

    print(password)

#Returns a list of strings
def get_strings(filepath):
    with open(filepath) as f:
        return f.read().split("\n")

#Returns the assembled password with special chars and numbers
def assemble_pw(word_list, char_list, pw_length):
    password = ""
    counter = 1
    #Randomize which word will be capitalized
    capitalize = random.randint(counter, pw_length)
    while counter <= pw_length:
        if counter == capitalize:
            password += random.choice(word_list).capitalize() + random.choice(char_list)
        else:
            password += random.choice(word_list) + random.choice(char_list)
        counter += 1
    #Cut the last special char for aesthetics
    return password[:-1]

if __name__ == "__main__":
    main()