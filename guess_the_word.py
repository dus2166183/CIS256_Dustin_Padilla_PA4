# Your Name
# CIS256 Fall 2026
# Programming Assignment 4
# A program that allows a user to play Hangman. Accepts a users input of a
# letter and tells the user if they guessed a correct letter by displaying
# the letters of the word at the correct index, and skipping letters they
# have not yet gussed. Ends when the user guesses the word, or finishes
# their 10th attempt

# PSEUDOCODE
#
# import random
#
# confirm_valid_input(userInput) function:
#   IF userInput is 1 letter
#       RETURN True
#   ELSE
#       RETURN False
#
#
# find_guess_in_hangmanWord(userInput, hangmanWord) function:
#   IF userInput in hangmanWord
#       RETURN True
#   ELSE
#       RETURN False
#
#
# display_found_letters(userGuessesList, hangmanWord) function:
#   foundAllLetters = False
#   numberOfCorrectLetters = 0
#   index = 0
#
#   While loop True
#       IF hangmanWord[index] in userGuessesList
#           DISPLAY hangmanWord[index] without a newline
#           numberOfCorrectLetters + 1
#           index + 1
#       ELSE
#           DISPLAY "_" without a newline
#           index + 1
#
#       IF numberOfCorrectLetters equals the length of hangmanWord
#           foundAllLetters = True
#
#       IF index equals the length of hangmanWord
#           BREAK loop
#
#   DISPLAY an empty newline for white spacing
#   RETURN foundAllLetters
#
#
# main() function:
#
#   hangmanWordList = []
#   hangmanWord = ""
#   userGuessesList = []
#   userInput = ""
#   attemptsReaming = 10
#
#   CALL random for int 0 - 9
#   hangmanWord = hangmanWordList[random int]
#
#   DISPLAY user greeting
#    
#   WHILE LOOP attemptsReaming is greater than 0
#       DISPLAY user INPUT request with forced lowercase
#    
#       IF user input is "stop", BREAK loop and DISPLAY taunting message
#
#       CALL confirmValidInput to confirm valid input
#           IF not valid, DISPLAY informative message and CONTINUE loop
#   
#       CALL a function to find user input in hangmanWord
#           IF not valid, -1 attemptsRemaining and DISPLAY informative message
#              and CONTINUE loop
#           ELSE add userInput to a list of userGuessesList
#   
#       CALL a function to display userGuesses found in hangmanWord
#           IF foundAllLetters = True, DISPLAY congratulatory message 
#              and BREAK loop
#   
#   IF attemptsReaming equals 0
#       DISPLAY consoling message
# END



import random

# Picks a random word to be our hangman word
def pick_a_random_word():
    randomWord = hangmanWordList[random.randint(0, 9)]
    return randomWord

# Checks if the user input is exactly one letter
def confirm_valid_input(guessedLetter):
    if len(guessedLetter) == 1 and guessedLetter.isalpha():
        return True
    else:
        return False


# Checks if user input is in the hangman word.
def find_guess_in_hangmanWord(guessedLetter, userGuessesList, hangmanWord):

    # Checks if the guessed letter is in the hangman word
    if guessedLetter in hangmanWord:
        return True
    else:
        return False


# Displays the found letters, at the correct index, in the hangman word
def display_found_letters(userGuessesList, hangmanWord):
    
    foundAllLetters = False
    numberOfCorrectLetters = 0 
    i = 0

    while True:
        # Finds the index of the found letters and prints them at their index
        # otherwise it prints a "_" if that index's letter has not been found
        if hangmanWord[i] in userGuessesList:
            print(hangmanWord[i], end=' ')
            numberOfCorrectLetters += 1
            i += 1
        else:
            print("_", end=' ')
            i += 1
            
        # Checks if the numberOfCorrectLetters is the same length as the word
        # and if so, the word has been found.
        if numberOfCorrectLetters == len(hangmanWord):
            foundAllLetters = True

        # Checks if the current index has reached the end of the hangman word
        if i == len(hangmanWord):
            break
        
    # Newline to get off the display_found_letters output line
    print()
    return foundAllLetters


# List needs to be visibile to be testable
hangmanWordList = ['HORSESHOE', 'TELEPORT', 'MOUNTAIN', 'NOTEBOOK',
                    'BLIZZARD', 'UMBRELLA', 'DINOSAUR', 'KEYBOARD',
                    'SANDWICH', 'TREASURE']


# Start main
def main():
    # Sets all needed variables
    ###
    # Realized as I started testing that the hangman list in in the main functions and thus
    # cant be tested. As I original planned, so I had to move it to its own function
    ###
    hangmanWord = ""
    userGuessesList = []
    userInput = ""
    attemptsRemaining = 10
    

    # Seclects a word at random from the hangman word list
    hangmanWord = pick_a_random_word()

    # Greets the user
    print("Welcome to\n \"Kind of Rude Hangmaaan!\"")
    print("A word has already been selected, start your guessing now!\n")

    while attemptsRemaining > 0:
    
        userInput = input("Please enter the letter you would like to guess: ")
        userInput = userInput.upper()

        if userInput == "STOP":
            print("Awwww, is someone scared to spell?")
            print("Thats okay, I hope you still have a great day")
            break

        if confirm_valid_input(userInput) == False:
            print("That was not a valid input. Please enter a single letter",
                  " or the word STOP in uppercase, as shown here.")
            continue

        if find_guess_in_hangmanWord(userInput, userGuessesList, hangmanWord) == False:
            attemptsRemaining -= 1
            print("That letter is not in the word, hahaha, that sucks.")
            continue
        else:
            userGuessesList.append(userInput)


        if display_found_letters(userGuessesList, hangmanWord) == True:
            print("... welp, you found all the letters. I really didn't think",
                  " you'd pull it off, sorry for doubting you. Congratulations.")
            break
   
    if attemptsRemaining == 0:
        print("And you are now out of attempts. Sorry champ, you didnt quite",
              " get the word!")

    print("Thanks for playing! Come back again if you think you can beat me!")
# END




