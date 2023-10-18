
import random

class Hangman:


    def __init__(self,word_list,num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        
        # Initialise the following attributes:
        # word_list, num_lives, word, word_guessed, num_letters & list_guesses

        # word_list is available in the game
        self.word_list = word_list 

        # number of lives is predefined to 5
        self.num_lives = num_lives 

        # select a random word from the word_list
        self.word = random.choice(word_list)

        # visualise the word length with "_"
        self.word_guessed = []
        for i in range(len(word)):
            word_guessed.append("_")

        # identify the number of unique characters
        self.num_letters = len(set(word))

        # store user inputs (guesses) in a list
        self.list_of_guesses = []

        
        # TODO 2: Print two message upon initialization:
        
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        print(f'The mistery word has {num_letters} unique characters')
        print(f'{word_guessed}')

    def check_guess(guess):
        # Check if the guessed letter is in the random selected word
        guess=str(guess).lower()
        if guess in word:
            print(f'Good guess! {guess} is in the word.')
            count=0
            for character in word:
                if character==guess:
                    word_guessed[count]=guess
                count+=1
            num_letters=num_letters-1
            

        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
            num_lives=num_lives-1
            print(f'You have {num_lives} lives left.')
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
                    
        if guess in list_of_guesses:
            print(f'You already tried that letter!')
        else:
            list_of_guesses.append(guess)
        return guess


check_guess(ask_for_input())


