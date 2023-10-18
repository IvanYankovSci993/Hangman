import random
word_list = ["bannana", "apple", "orange", "kiwi", "mango"]
print((word_list))
word=random.choice(word_list)
print(word)
# ask the user to guess a letter
print("Guess a letter:")
guess=input()
# check if the guess is 1 character long and if it is alnum
if len(guess)==1 and guess.isalnum():
        print(guess)
else:
        print("Oops! That is not a valid input")