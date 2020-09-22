import requests
from bs4 import BeautifulSoup
from tkinter import filedialog

def get_preterito_forms(word):
    url = "https://www.wordreference.com/conj/EsVerbs.aspx"

    if is_reflexive_verb(word):
        reflexive = True
        word = word[0:-2]
    else:
        reflexive = False

    pronouns = ["me", "te", "se", "nos", "os", "se"]

    data = {'v': word}

    req = requests.get(url, params=data);
    soup = BeautifulSoup(req.text, features="html.parser")
    noodles = soup.find_all("table")

    possible_answers = []

    for element in noodles:
        element = element.find_all("td")

        for thing in element:  
            #'< 3' to avoind very big chunks of html 
            if len(thing) < 3:
                possible_answers.append(thing.get_text())

    if reflexive:
        for i in range(15,21):
            possible_answers[i] = pronouns[i-15]+ ' ' + possible_answers[i]


    return possible_answers[15:21]


def is_file_valid(path):
    if path != '' and path[-4:] == ".txt":
        return True
    else:
        return False


def get_word_list_from_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()

    return lines


def is_reflexive_verb(word):
    if word[-2:] == "se":
        return True
    else:
        return False


def print_output(data):
    print("-----------------------------------\n")

    for key, value in data.items():
        print(f"{key}:")
        for item in value:
            print(f"| {item}")
        print()


    print("---------------------------------")





print("*********************************")
print("""Spanish verb conjugator - program that conjugates spanish verbs, currently only for "pretérito"
  Created by NotSirius-A
  Open source, for public use

  Author: https://github.com/NotSirius-A
  Source Code: https://github.com/NotSirius-A/Spanish-verb-conjugator

  Version - 1.0 """)
print("*********************************")
print("Enter \"exit\" to quit. \n")


while True:

    choice = input("Enter 'f' for File mode or 'i' for Input mode: ")

    if choice == 'i':

        input_word = input("Word: ")

        answer = {}
        answer[input_word] = get_preterito_forms(input_word)

        print_output(answer)

    elif choice == 'f':
        file_path = filedialog.askopenfilename()

        if is_file_valid(file_path):

            word_list = get_word_list_from_file(file_path)
            
            answers = {}

            for word in word_list:
                word = word.replace('\n', '') 

                answers[word] = get_preterito_forms(word)
                
            print_output(answers)

        else:
            print('Choose a valid *.txt file')

    elif choice == "exit":
        exit()
    else:
        print("Please enter 'f' or 'i'")







