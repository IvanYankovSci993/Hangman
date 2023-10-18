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

    # def check_letter(self, letter) -> None:
    #     '''
    #     Checks if the letter is in the word.
    #     If it is, it replaces the '_' in the word_guessed list with the letter.
    #     If it is not, it reduces the number of lives by 1.

    #     Parameters:
    #     ----------
    #     letter: str
    #         The letter to be checked

    #     '''
    #     # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
    #     # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
    #     # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
    #     # TODO 3: If the letter is not in the word, reduce the number of lives by 1
    #     # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
    #     pass

    def check_guess(self,guess):
        # Check if the guessed letter is in the random selected word
        self.guess=str(self.guess).lower()
        if self.guess in word:
            print(f'Good guess! {self.guess} is in the word.')
            count=0
            for character in word:
                if character==self.guess:
                    self.word_guessed[count]=self.guess
                count+=1
            self.num_letters=self.num_letters-1
            

        else:
            print(f'Sorry, {self.guess} is not in the word. Try again.')
            self.num_lives=self.num_lives-1
            print(f'You have {self.num_lives} lives left.')
        pass

    # def ask_letter(self):
    #     '''
    #     Asks the user for a letter and checks two things:
    #     1. If the letter has already been tried
    #     2. If the character is a single character
    #     If it passes both checks, it calls the check_letter method.
    #     '''
    #     # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
    #     # TODO 1: Assign the letter to a variable called `letter`
    #     # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
    #     # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
    #     # TODO 3: If the letter is valid, call the check_letter method
    #     pass

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
        
        pass

# def play_game(word_list):
#     # As an aid, part of the code is already provided:
#     game = Hangman(word_list, num_lives=5)
#     # TODO 1: To test this task, you can call the ask_letter method
#     # TODO 2: To test this task, upon initialization, two messages should be printed 
#     # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
#     # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
#     # If the user guesses the word, print "Congratulations! You won!"
#     # If the user runs out of lives, print "You lost! The word was {word}"

#     pass

def play_game(word_list):
    num_lives=5
    game=Hangman(word_list,num_lives)
    # game(word_list,num_lives)
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
