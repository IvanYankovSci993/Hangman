import random
word_list = ["bannana", "apple", "orange", "kiwi", "mango"]
print((word_list))
word=random.choice(word_list)
print(word)
print("Guess a letter:")
guess=input()
if len(guess)==1 and guess.isalnum():
        print(guess)
else:
        print("Oops! That is not a valid input")