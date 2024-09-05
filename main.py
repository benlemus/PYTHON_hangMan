import random
from termcolor import colored

# WORD TO BE GUESSED
words = ['hello', 'word', 'kori', 'marvin', 'milo', 'mojo', 'cute', 'mouse']

word_to_be_guessed = []
state_of_guessed = []
no_color_state = []

# GUESSED
letters_guessed = []
num_incorrect = 0

# GUESSING ACTIVITY
guessing_active = True
convert_word = True

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


def show_game():

    all_lines = [line1, line2, line3, line4, line5, line6, line7]

    for line in all_lines:
        for char in line:
            print(char)


def checks_letter_guessed(guess):
    # checks if letter is in alphabet
    if guess in alphabet:
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            if guess in word_to_be_guessed:
                return True
                
            else:
                global num_incorrect
                num_incorrect += 1
                return False
        else:
            print(colored('\n !! LETTER ALREADY GUESSED !!', 'light_blue'))
    else:
        print(colored('\n !! ENTER VALID LETTER !!', 'light_blue'))

def get_word_to_be_guessed():
    length_of_word_bank = len(words)

    random_int = random.randint(1,length_of_word_bank)

    return words[random_int - 1]

def updates_word_to_be_guessed(word):
    global word_to_be_guessed
    word_to_be_guessed = list(word)
    

def updates_word_state(guess):

    for char in word_to_be_guessed:
       if char == guess: 
        char_indx = word_to_be_guessed.index(char)
        state_of_guessed[char_indx] = colored(guess, 'green')
        no_color_state[char_indx] = guess


def shows_word_state():
    global convert_word

    if convert_word:
        for char in word_to_be_guessed:
            state_of_guessed.append('_')
            no_color_state.append('_')
        convert_word = False
    
    state_of_guessed_str = ' '.join(state_of_guessed)
    print(f'Word To Be Guessed: {state_of_guessed_str}')
        
def shows_letters_guessed():
    letters_guessed_to_str = ', '.join(letters_guessed)

    letters_guessed_count = len(letters_guessed)

    print(f'Letters Guessed({letters_guessed_count}): {letters_guessed_to_str}')

def update_board(is_correct):
    if is_correct == True:
        return 
    elif is_correct == False:
        global num_incorrect
        a = num_incorrect

        global line3
        global line4
        global line5
        global line6

        if a == 1:
            line3 = [f"    |     {colored('O', 'red')}"]
        elif a == 2:
            line4 = [f"    |     {colored('|', 'red')}"]
        elif a == 3:
            arm = '|/'
            line4 = [f"    |     {colored(arm, 'red')}"]
        elif a == 4:
            double_arms = '\|/'
            line4 = [f"    |    {colored(double_arms, 'red')}"]
        elif a == 5:
            line5 = [f"    |     {colored('|', 'red')}"]
        elif a == 6:
            leg = '\\'
            line6 = [f"    |      {colored(leg, 'red')}"]
        elif a == 7:
            double_legs = '/ \\'
            line6 = [f"    |    {colored(double_legs, 'red')}"]

    
def guess_promt():

    guess = input('Enter Guess: ').lower()
    print('\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
    
    return guess


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
        

    
def end_game():
    global guessing_active
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global word_to_be_guessed
    global state_of_guessed
    global letters_guessed
    global num_incorrect
    global convert_word
    
    guessing_active = False

    show_game()

    print(colored('Game Over!!', 'red'))

    shows_letters_guessed()
            
    play_again_promt = input(f"Press {colored('ENTER', 'green')} to play again \nPress {colored('Q', 'green')} then {colored('ENTER', 'green')} to exit.")
    if play_again_promt == '':

        guessing_active = True

        line1 = ["     _____"]
        line2 = ["    |     |"]
        line3 = ['    |     ']
        line4 = ['    |    '] 
        line5 = ['    |     ']
        line6 = ["    |    "]
        line7 = [" ___|___"]

        word_to_be_guessed = []
        state_of_guessed = []


        letters_guessed = []
        num_incorrect = 0

        convert_word = True

        main()
    if play_again_promt == 'q':
        pass

def shows_win():
    global guessing_active

    guessing_active = False

    show_game()

    shows_word_state()

    shows_letters_guessed()

    print(colored('YOU WIN!!', 'green'))

        
def main():
    word = get_word_to_be_guessed()

    updates_word_to_be_guessed(word)

    global guessing_active
    global current_guess
    global letters_guessed
    global no_color_state

    while guessing_active == True:
        show_game()

        shows_word_state()

        shows_letters_guessed()

        guess = guess_promt()

        if guess == '**':
            guessing_active = False
            break
      
        is_correct = checks_letter_guessed(guess)

        if is_correct:
            updates_word_state(guess)
            char_indx = letters_guessed.index(guess)
            letters_guessed[char_indx] = colored(guess, 'green')
            print(colored('\n| correct |\n', 'green'))
        else:
            char_indx = letters_guessed.index(guess)
            letters_guessed[char_indx] = colored(guess, 'red')
            print(colored('\n| incorrect |\n', 'red'))

        update_board(is_correct)
        
        if no_color_state == word_to_be_guessed:
            shows_win()
            # print(colored('YOU WIN!!', 'green'))
            # guessing_active = False
        

        global num_incorrect
        if num_incorrect == 7:
            end_game()

        # ADD WHEN YOU WIN

if __name__ == "__main__":
     main()





# line1 = ["     _____"]
# line2 = ["    |     |"]
# line3 = ['    |     O']
# line4 = ['    |    \|/']
# line5 = ['    |     |']
# line6 = ["    |    / \\"]
# line7 = ["____|____"]