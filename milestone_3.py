import random
word_list = ["bannana", "apple", "orange", "kiwi", "mango"]
word=random.choice(word_list)
            
def check_guess(guess):
    # Check if the guessed letter is in the random selected word
    guess=str(guess).lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
    pass

def ask_for_input():

    # Iteratively check if the input is a valid guess
    i=True
    while i is True:
        print("Guess a letter:")
        guess=input()
        # check if the guess is 1 character long and if it is alpha
        if len(guess)==1 and guess.isalpha():
                print(guess)
                i=False
                break
        else:
                print('Oops!Invalid letter.'+'\n'+
                    'Please, enter a single alphabetical character.')
    return guess

check_guess(ask_for_input())