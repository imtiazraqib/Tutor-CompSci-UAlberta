#WordPuzzle V1
#This version plans to implement the ability for the program to select a word from a limited word list
#The program will then remove the first letter and replace it with an _ and the player can make a guess
#if correct, the program congratulates. if not then condolensces are sent
#Functions such as multiple guesses and multiple _ in place of letters will be absent
#V2 will be implementing full word removal and replacement with _. The user will also have multiple tries(2)
#

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
    length_word = len(random_word)
    puzzle = []
    
    #method used to replace each letter with _    
    for i in range(length_word):
        puzzle.append("_ ")
        
    #display the word so far (should be blank with just underscores)    
    print('The answer so far is ', end='')
    for i in range(length_word):
        print(puzzle[i], end='')
    print()  
    
    #get players input, using temp setting to register if player does not match letter with one within random word
    player_input = input("Guess the letter: ")
    temp=False
    
    #for loop to see if the player has input a letter that is residing within the random word
    for i in range(length_word):
        if player_input.lower() == random_word[i].lower():
            puzzle[i]=player_input.lower()
            temp=True
    #if the given letter is correct, the if statement inputs the players response and replaces the underscores         
    string_form = ' '.join(puzzle)
    if temp == True:
        print(string_form)
        print('Good job! You found the word ' + random_word + '!')
    
    #if incorrect, the underscores will not be replaced    
    else:
        print(string_form)
        print('Not quite, the correct word was ' + random_word + '. Better luck next time')
       
   
    #end game function
    input('Press enter to end the game.')

main()

