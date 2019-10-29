#WordPuzzle V1
#This version plans to implement the ability for the program to select a word from a limited word list
#The program will then remove the first letter and replace it with an _ and the player can make a guess
#if correct, the program congratulates. if not then condolensces are sent
#Functions such as multiple guesses and multiple _ in place of letters will be absent
#V2 will be implementing full word removal and replacement with _. The user will also have multiple tries(2)
# V3 will implement all of the features such as word replacement, word checking, multiple user functions, and all previous functions implemented

import random

def main():
    #this function prints the instructions
    display_instructions("instructions Wordpuzzle.txt")
    
    #the word list and the method used to replace the word with _
    wordbank = ['mango', 'banana', 'watermelon', 'kiwi']
    random_word = random.choice(wordbank)
    length_word = len(random_word)
    puzzle = []
    #find length of random word and replace with underscore
    for i in range(len(random_word)):
        puzzle.append("_ ")
    #answer so far prompt
    print('The answer so far is ', end='')
    for i in range(len(puzzle)):
        print(puzzle[i], end='')
    print()
    #status received from other code in order to check the status of the word 
    statusReceived = play_game(puzzle, random_word)
    
    if statusReceived == False:
        display_results(False, random_word)
    
    else:
        display_results(True, random_word)
    input('Press enter to end the game.')

#displays instructions
def display_instructions(filename):
 #This prints the instructions to the game
    instructions_file = open(filename, "r")
    file_contents = instructions_file.read()
    instructions_file.close()
    print(file_contents)


def display_puzzle_string(puzzle):
    #print the current state of the guess and word
    print('The answer so far is ', end='')
    for i in range(len(puzzle)):
        print(puzzle[i], end='')
    print()

def play_game(puzzle, answer):
    #guesses for player left
    guesses = 4
    check = 0
    
    #used to check if the player has successfully guessed the word, by checking the status of the word and updating the list
    while check != 1:
        playerInput = get_guess(guesses)
        updatedPuzzle = update_puzzle_string(puzzle, answer, playerInput)
        display_puzzle_string(updatedPuzzle[0])
        #structure used to remove a guess left for a word
        if updatedPuzzle[1] == False:
            guesses -= 1
        if guesses == 0:
            break
        
        guessedWord = "".join(updatedPuzzle[0])
        if guessedWord == answer.lower():
            break
    
    status = is_word_found(updatedPuzzle[0])
    
    return status
                   
                   
def get_guess(num_guesses):
    #code for showing how many guesses remain
    guessedWord = input("Guess the letter (" + str(num_guesses) + " guesses remaining): ")
    return guessedWord

def update_puzzle_string(puzzle, answer, guess):
    #checking the string that is guessed and sending the status to earlier code
  
    correctGuess = False
    for i in range(len(answer)):
        if guess.lower() == answer[i].lower():
            if guess.lower() not in puzzle:       
                correctGuess = True
            puzzle[i] = guess.lower()
            
    
            
    return puzzle, correctGuess

        
def is_word_found(puzzle):
    #checking if the word has been found by seeing if there are any _ left
    for i in range(len(puzzle)):
        if puzzle[i] == "_ ":
            return False
    
    return True
    
    
def display_results(is_win, answer):
    #win statements or loss statements
    if is_win == True:
        print("Good job! You found the word " + answer)
    
    else:
        print("Not quite, the correct word was " + answer + ". Better luck next time!")
main()
    