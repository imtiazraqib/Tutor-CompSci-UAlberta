#WordPuzzle V1
#This version plans to implement the ability for the program to select a word from a limited word list
#The program will then remove the first letter and replace it with an _ and the player can make a guess
#if correct, the program congratulates. if not then condolensces are sent
#Functions such as multiple guesses and multiple _ in place of letters will be absent

import random


def main():
    #This prints the instructions to the game
    instructions_file = open("instructions Wordpuzzle.txt", "r")
    file_contents = instructions_file.read()
    instructions_file.close()
    print(file_contents)
    
    #the word list and the method used to delete the first letter
    wordbank = ['Mango', 'Banana', 'Watermelon', 'Kiwi']
    random_word = random.choice(wordbank)
    rest_of_random = random_word[1:]
    guess = '_' + rest_of_random
    
    #prompts user for a guess
    print("The answer so far is " )
    print(guess)
    player_input = input("Guess the letter: ")
    
    #method used to remove all but the first letter in order to match player input
    first_of_random = random_word[:1]    
    if player_input.lower() == first_of_random.lower():
        print('Good job! You found the word ' + random_word + '!')
    else:
        print('Not quite, the correct word was ' + random_word + '. Better luck next time')
        
    input('Press enter to end the game.')

main()