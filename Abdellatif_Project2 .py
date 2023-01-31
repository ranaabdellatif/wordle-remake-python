"""
In this project I will be re-creating a python version of the famous game, "Wordle".

File Name: Abdellatif_Project2 .py
Author: Rana Abdellatif
Date: 01/16/2023
Course: COMP 1352
Assignment: Project 2 - A Word Game
Collaborators: None
Internet Source: None

"""
import random
#empty lists to append & filter words from dictionary
usa_words = []
five_letters = []
count = 1
#reads dictionary by line and extracts each word
with open("Projects/Abdellatif_Project2/usa.txt" , 'r') as a_file:
    for line in a_file:
        usa_words.append(line.strip())

#filters out dictionary to only words with five letters
for i in range(len(usa_words)):
    if len(usa_words[i]) == 5:
        five_letters.append(usa_words[i])

#function to generate a random word from the list
def generate_word(a_list: list)->str:
    word = random.choice(a_list)
    return word

#user input for word and generates computer word
comp_word = generate_word(five_letters)
user_word = input("Welcome to the game Wordle! Your goal is to guess the five letter word.\nIf the letter is in the correct place, the computer will output a 'G'.\nIf the letter is in the word, but the incorrect place, the computer will output 'Y'.\nIf the letter is not in the word, the computer will output 'B'. You have 6 tries, good luck!\nEnter your first word:")
if user_word not in five_letters:
    user_word = input("This is not a valid word, please try again: ")

#function to play game
def play_wordle(comp: str, user: str)->None:
    for i in range(len(user_word)):
        if user_word[i] == comp_word[i]:
            print("G", end="")
        elif user_word[i] in comp_word:
            print("Y", end="")
        else:
            print("B", end="")
    

#loop to end the game when someone wins or when 6 guesses are used
while comp_word != user_word and count <= 5:
    count +=1
    print(f'Guess {count}: {user_word} ', end="")
    play_wordle(comp_word,user_word)
    user_word = input(" ")
    if user_word not in five_letters:
        user_word = input("This is not a valid word, please try again: ")

if user_word == comp_word:
    print(f"\nYou win! It took you {count} guesses")
else:
    print(f"You used up your 6 guesses! The word was: {comp_word}")