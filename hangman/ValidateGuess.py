'''
    Function to check if a valid guess


    Args:
        NULL
    
    Returns:
        string
'''

def ValidateGuess():
    while True:
        player_guess = input("Enter a letter: ")

        if len(player_guess) != 1:
            print("Invalid guess, please try again")
        elif player_guess.isalpha() == False:
            print("Your guess must be a letter")
        else:
            return player_guess
        