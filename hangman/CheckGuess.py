'''
    Check if the guessed letter is in the secret word

    Args:
        player_guess (str): guessed letter from the player
        secret_word (str): word the player is trying to guess
        hidden_word (str): String for the secret word with guessed letters

    Returns:
        string
'''

def CheckGuess(player_guess: str, secret_word: str, hidden_word: str) -> str:
    #Check player guessed letter versus the hidden word to see if there is a match

    new_hidden_word = ""
    for letter in range(len(hidden_word)):
        if player_guess == secret_word[letter]:
            new_hidden_word += player_guess
        else:
            new_hidden_word += hidden_word[letter]
    
    return (new_hidden_word)

