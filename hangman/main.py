'''A hangman game with a list of secret words'''
import os
import GetSecret
import HideWord
import ValidateGuess
import Noose
import CheckGuess



#main game loop
playing = True

while playing:
    lives = 6
    secret = GetSecret.GetSecret()
    hidden_word = HideWord.Hide(secret)
    
    player_guess = ''

    #new game loop
    game_over = False
    while not game_over:
        #Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
 
                 /$$   /$$                                                                
                | $$  | $$                                                                
                | $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ 
                | $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
                | $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
                | $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
                | $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
                |__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                                               /$$  \ $$                                  
                                              |  $$$$$$/                                  
                                               \______/                                   
 
""")

        Noose.Noose_Pic(lives)
        print(f"{hidden_word}                                   Lives: {lives}")

        if lives == 0:
            print(f"The secret word was: {secret}")
            game_over = True
        elif hidden_word == secret:
            print(f"You guessed the secret word: {secret}")
            game_over = True
        else:    
            player_guess = ValidateGuess.ValidateGuess()
            checkedGuess = CheckGuess.CheckGuess(player_guess, secret, hidden_word, lives)

            hidden_word = checkedGuess[0]
            lives = checkedGuess [1]

        
    replay = input("Would you like to play again(y/n): ").lower()
    while replay not in ("n","y","no", "n"):
        replay = input("Please enter y/n or yes/no): ").lower()
    if replay in ('n', 'no'):
        playing = False
        