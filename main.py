import random

# WORD TO BE GUESSED
words = ['hello', 'word', 'kori', 'marvin', 'milo', 'mojo', 'cute', 'mouse']

word_to_be_guessed = []
state_of_guessed = []

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
            print('\n !! LETTER ALREADY GUESSED !!')
    else:
        print('\n !! ENTER VALID LETTER !!')

def get_word_to_be_guessed():
    length_of_word_bank = len(words)

    random_int = random.randint(1,length_of_word_bank)

    return words[random_int - 1]

def updates_word_to_be_guessed(word):
    global word_to_be_guessed
    word_to_be_guessed = list(word)
    

def updates_word_state(guess):
    indx_of_guess = 0

    for char in word_to_be_guessed:
       indx_of_guess += 1
       if char == guess: 
        new_indx = indx_of_guess - 1
        state_of_guessed[new_indx] = guess

def shows_word_state():
    global convert_word

    if convert_word:
        for char in word_to_be_guessed:
            state_of_guessed.append('_')
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
            line3 = ['    |     O']
        elif a == 2:
            line4 = ['    |     |']
        elif a == 3:
            line4 = ['    |     |/']
        elif a == 4:
            line4 = ['    |    \|/']
        elif a == 5:
            line5 = ['    |     |']
        elif a == 6:
            line6 = ["    |      \\"]
        elif a == 7:
            line6 = ["    |    / \\"]

    
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
    

        
def main():
    # GET WORD
        # updates word_to_be_guessed
    word = get_word_to_be_guessed()

    updates_word_to_be_guessed(word)

    global guessing_active

    while guessing_active == True:
        show_game()

        shows_word_state()

        shows_letters_guessed()

        guess = guess_promt()
      
        is_correct = checks_letter_guessed(guess)

        update_board(is_correct)
        
        if guess == '**':
            break

        if is_correct:
            updates_word_state(guess)
            print('\n| correct |\n')
        else:
            print('\n| incorrect |\n')


        global num_incorrect
        if num_incorrect == 7:
            guessing_active = False

            show_game()

            print('Game Over!!')

            shows_letters_guessed()
            
            print('Press ENTER to play again')
            print('Press Q then ENTER to exit.')

            play_again_promt = input('')

            if play_again_promt == '':
                guessing_active = True
                main()
            if play_again_promt == 'q':
                pass

        # ADD WHEN YOU WIN

if __name__ == "__main__":
     main()





# line1 = ["     _____"]
# line1 = ["    |     |"]
# line1 = ['    |     O']
# line5 = ['    |    \|/']
# line5 = ['    |     |']
# line5 = ["    |    / \\"]
# line5 = ["____|____"]