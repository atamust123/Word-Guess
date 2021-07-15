# -*- coding: utf-8 -*-
import sys
import time


#   My program creates dictionaries for correct_words and letter_values.
# correct_letters has a key it stores right hand side of ":"
# and value it is another dictionary.Its keys are correct form of words
# and its values are 1 or 0. 1 means this word is not guessed. 0 means
# this word is guessed before and marked
# dict_for_correct_letters= { shuffled letter : {correct forms : ( 1 or 0 ) } }

def calculate_score(guessed):
    total_score = 0
    for i in guessed:
        total_score += dict_for_letter_values.get(i)
    return total_score*len(guessed_word)


try:
    f = open(sys.argv[1], "r", encoding="utf-8-sig")
    f2 = open(sys.argv[2], "r", encoding="utf-8-sig")
except:
    print("You must write two arguments for this program")
    exit()

a = []  # Splitting lines to create dictionary
dict_for_letter_values = {}  # letter values will store in here
dict_of_correct_letters = {}  # correct_word_letters will store in it
for i in f:
    b = i.split()
    if len(b) > 0:  # to ignore blank lines of inputs
        a.append(b[0].split(":"))

for i in a:  # create dictionary for correct letters
    temp_list = i[1].split(",")
    temp_dict = {i.upper(): 1 for i in temp_list}
    dict_of_correct_letters.update({i[0].upper(): temp_dict})
a.clear()

for i in f2:
    a.append(i.split("\n")[0].split(":"))
for i in a:
    dict_for_letter_values.update({i[0].upper(): int((i[1]))})
counter = 0

for k in dict_of_correct_letters:  # iterate until all correct words of all shuffled letters are guessed
    print("Shuffled letters are:    " + k, "Please guess words for these letters with"
                                           "minium three letters")
    total = 0
    current = time.time()
    while 1 in dict_of_correct_letters.get(k).values():  # iterate until correct words of a shuffled letters are guessed
        guessed_word = input("Guessed word: ").replace(u"i", u"İ").upper()
        now = time.time()
        if (now - current) >= 29 or (1 not in dict_of_correct_letters.get(k).values() ):
            print("You have 0 time")
            print("Score for", k, "is", total, end=" ")
            if total == 0:
                print()
            else:
                print("and guessed words are: ", end="")
                all_guessed = []
                for k, v in dict_of_correct_letters.get(k).items():
                    if v == 0:
                        all_guessed.append(k)
                print("-".join(all_guessed))
            break
        else:
            print("You have ", str(int(30 - now + current)), "time")
        if dict_of_correct_letters.get(k).__contains__(guessed_word):
            if dict_of_correct_letters.get(k).get(guessed_word) == 1:  # if the guessed word is not guessed before
                dict_of_correct_letters.get(k)[guessed_word] = 0  # assign word as guessed
                total += calculate_score(guessed_word)  # calculate score
            else:
                print("This word is guessed before")
        else:
            print("Your guessed word is not valid word")

f.close()
f2.close()
