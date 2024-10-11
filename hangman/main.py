'''A hangman game with a list of secret words'''
import GetSecret
import HideWord
import ValidateGuess


#main game loop
playing = True
lives = 5

while playing:
    secret = GetSecret.GetSecret()
    hidden_word = HideWord.Hide(secret)
    
    player_guess = ''

    #new game loop
    word_guessed = False
    while not word_guessed:
        
        player_guess = ValidateGuess.ValidateGuess()
        


