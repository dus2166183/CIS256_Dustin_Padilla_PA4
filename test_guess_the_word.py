from guess_the_word import(
    hangmanWordList, pick_a_random_word, confirm_valid_input,
    find_guess_in_hangmanWord, display_found_letters)


# Testing if the selected random word is from a predetermined list
# arguments = null
def test_pick_random_word():
    # Repeating the test mutliple times since the slections is random
    for i in range(500):
        # Checks if the random word is in hangmanWordList
        assert pick_a_random_word() in hangmanWordList
        

# Testing confirm_valid_input function
# arguments = guessedLetter
def test_single_char_input():
    assert confirm_valid_input("X") is True

def test_empty_char_input():
    assert confirm_valid_input(" ") is False

def test_string_input():
    assert confirm_valid_input("XY") is False

def test_numeric_input():
    assert confirm_valid_input("1") is False


# Testing find_guess_in_hangmanWord function
# arguments = guessedLetter, userGuessesList, hangmanWord
def test_find_guess_in_hangmanWord_with_correct_guess():
    assert find_guess_in_hangmanWord("A", [], "APPLE") is True
    
def test_find_guess_in_hangmanWord_with_repeated_guess():
    assert find_guess_in_hangmanWord("P", ["P"], "APPLE") is True

def test_find_guess_in_hangmanWord_with_incorrect_guess():
    assert find_guess_in_hangmanWord("Z", [], "APPLE") is False


# Testing display_found_letters function
# arguments = userGuessesList, hangmanWord
#def test_display_shows_blanks():
#    assert display_found_letters([], "CAT") == "_ _ _ \n"
    # I found I can not test a string output with the knowledge I have, and
    # could not find a how to guide on
    # https://docs.pytest.org/en/stable/how-to/index.html#how-to
def test_not_all_letters_found():
    assert display_found_letters(["D"], "DRIP") == False

def test_not_all_letters_found():
    assert display_found_letters(["D", "I", "P", "R"], "DRIP") == True
