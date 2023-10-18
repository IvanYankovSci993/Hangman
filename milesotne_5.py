'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self,word_list,num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        
        # Initialise the following attributes:
        # word_list, num_lives, word, word_guessed, num_letters & list_guesses

        # word_list is available in the game
        self.word_list = word_list 

        # number of lives is predefined to 5
        self.num_lives = num_lives 

        # select a random word from the word_list
        self.word = random.choice(self.word_list)

        # visualise the word length with "_"
        self.word_guessed = []
        for i in range(len(self.word)):
            self.word_guessed.append("_")

        # identify the number of unique characters
        self.num_letters = len(set(self.word))

        # store user inputs (guesses) in a list
        self.list_of_guesses = []

        
        # TODO 2: Print two message upon initialization:
        
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        print(f'The mistery word has {self.num_letters} unique characters')
        print(f'{self.word_guessed}')

 

    def check_guess(self,guess):
        # Check if the guessed letter is in the random selected word
        self.guess=str(self.guess).lower()
        if self.guess in self.word:
            print(f'Good guess! {self.guess} is in the word.')
            count=0
            for character in self.word:
                if character==self.guess:
                    self.word_guessed[count]=self.guess
                count+=1
            self.num_letters=self.num_letters-1
            print(self.word_guessed)
            print(self.num_letters)
        else:
            print(f'Sorry, {self.guess} is not in the word. Try again.')
            self.num_lives=self.num_lives-1
            print(f'You have {self.num_lives} lives left.')
        pass


    def ask_for_input(self):
        # Iteratively check if the input is a valid guess
        i=True
        while i is True:
            print("Guess a letter:")
            self.guess=input()
            # check if the guess is 1 character long and if it is alpha
            if len(self.guess)==1 and self.guess.isalpha():
                print(self.guess)
                i=False
                break
            else:
                    print('Oops!Invalid letter.'+'\n'+
                        'Please, enter a single alphabetical character.')
                    
        if self.guess in self.list_of_guesses:
            print(f'You already tried that letter!')
        else:
            self.list_of_guesses.append(self.guess)
            print(self.list_of_guesses)
            self.check_guess(self.guess)
        pass


def play_game(word_list):
    num_lives=5
    game=Hangman(word_list,num_lives)
    while True:
        if game.num_lives==0:
            print("You lost!")
            break
        elif game.num_letters>0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
    pass

if __name__ == '__main__':
    word_list = ["bannana", "apple", "orange", "kiwi", "mango"]  
    play_game(word_list)
