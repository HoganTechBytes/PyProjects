'''A hangman game with a list of secret words'''
import GetSecret


#main game loop
playing = True

while playing:
    secret = GetSecret.GetSecret()
    hidden_word = ''
    for letter in secret:
        hidden_word += '_'
        

print(hidden_word)