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
