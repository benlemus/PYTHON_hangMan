# WORD TO BE GUESSED
        # HAVE BANK OF WORDS AND INSTEAD OF ENTERING, IT AUTO PICKS RANDOM WORD AND STARTS
word_to_be_guessed = ['h','e','l','l','o']
state_of_guessed = ['_','_','_','_','_']

# GUESSED
letters_guessed = []

# ALPHABET
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# LIST PER LINE FOR THING THAT HANGS PERSON/ PERSON

line1 = ["     _____"]
line2 = ["    |     |"]
line3 = ['    |     ']
line4 = ['    |    '] 
line5 = ['    |     ']
line6 = ["    |    "]
line7 = [" ___|___"]

all_lines = [line1, line2, line3, line4, line5, line6, line7]

def show_game():
    for line in all_lines:
        for char in line:
            print(char)

def changes_letter(guess):
    letter = guess


def checks_letter_guessed(guess):
    # checks if letter is in alphabet
    if guess in alphabet:
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess in word_to_be_guessed:
                return True
                
            else:
                return False
        else:
            print('LETTER ALREADY GUESSED')
    else:
        print('ENTER VALID LETTER')

def updates_word_state(guess):
    indx_of_guess = 0

    for char in word_to_be_guessed:
       indx_of_guess += 1
       if char == guess: 
        new_indx = indx_of_guess - 1
        state_of_guessed[new_indx] = guess
        

         
            
    
    
def guess_promt():
    guess = input('ENTER GUESS: ').lower()

    is_correct = checks_letter_guessed(guess)

    if is_correct:
        print('correct')
        updates_word_state(guess)
       
    else:
        print('incorrect')


            # calls to show updated game and promts guess again
        # if not correct, tells user, calls to check/update person, calls to show updated game and promts guess again
       

def start_game():
    # show underscores of each letter

    # show game
    show_game()

    # asks for guess
    guess_promt()



# CHECKS FOR PERSON

def checks_for_head(line):
    for char in line:
        if 'O' in char:
            return 'Full'
        else:
            return False

def checks_for_arms(line):
    for char in line:
        if '|' in char and '\\' not in char and '/' not in char:
            return 'back'
        elif '|' and '\\' in char and '/' not in char:
            return 'back_right_arm'
        elif '|' and '\\' and '/' in char:
            return 'full'
        else:
            return False

def checks_for_legs(line):
    for char in line:
        if '\\' in char and '/' not in char:
            return 'right_leg'
        if '/' and '\\' in char:
            return 'full'
        else:
            return False
    

# ADDS PERSON

    # HEAD
def add_head():
    return ['    |     O']

    # ARMS
def add_back_arm():
    return ['    |     |']

def add_right_arm():
    return ['    |     |/']

def add_full_arms():
    return ['    |    \|/']

    # BACK
def add_back():
    return ['    |     |']

    # LEGS
def add_right_leg():
    return ["    |      \\"]

def add_full_legs():
    return ["    |    / \\"]

        

# line1 = ["     _____"]
# line1 = ["    |     |"]
# line1 = ['    |     O']
# line5 = ['    |    \|/']
# line5 = ['    |     |']
# line5 = ["    |    / \\"]
# line5 = ["____|____"]


