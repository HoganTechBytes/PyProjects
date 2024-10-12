'''A hangman game with a list of secret words'''
import os
import GetSecret
import HideWord
import ValidateGuess
import Noose
import CheckGuess



#main game loop
playing = True
lives = 6

while playing:
    secret = GetSecret.GetSecret()
    hidden_word = HideWord.Hide(secret)
    
    player_guess = ''

    #new game loop
    word_guessed = False
    while not word_guessed:
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
        print(hidden_word)
        player_guess = ValidateGuess.ValidateGuess()
        hidden_word = CheckGuess.CheckGuess(player_guess, secret, hidden_word)

        