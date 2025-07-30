from random import randint, choice
from tkinter import Tk
from tkinter import messagebox
from constants import *

def main():

    password = assemble_pw(get_strings(WORD_LIST), get_strings(CHAR_LIST), PASSWORD_LENGTH)
    
    addToClipBoard(password)


#Returns a list of strings
def get_strings(filepath):
    with open(filepath) as f:
        return f.read().split("\n")

#Returns the assembled password with special chars and numbers
def assemble_pw(word_list, char_list, pw_length):
    password = ""
    counter = 1
    #Randomize which word will be capitalized
    capitalize = randint(counter, pw_length)
    while counter <= pw_length:
        if counter == capitalize:
            password += choice(word_list).capitalize() + choice(char_list)
        else:
            password += choice(word_list) + choice(char_list)
        counter += 1
    #Cut the last special char for aesthetics
    return password[:-1]

def addToClipBoard(string):
    #Get the string into the clipboard and show message with string
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(string)
    messagebox.showinfo("Password", f"The new password \n\n\"{string}\" \n\nhas been added to youre clipboard")
    r.update() #To keep password in clipboard after the window closes
    r.destroy()
    
if __name__ == "__main__":
    main()