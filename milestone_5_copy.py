def play_game(word_list):
    num_lives=5
    game=Hangman()
    game(word_list,num_lives)
    while True:
        if num_lives=0:
            print("You lost!")
            break
        elif num_letters>0:
            ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break
    pass

word_list = ["bannana", "apple", "orange", "kiwi", "mango"]   
play_game(word_list)