'''
    Function to check if a valid guess


    Args:
        NULL
    
    Returns:
        string
'''

def ValidateGuess() -> str:
    while True:
        player_guess = input("Enter a letter: ").lower()

        if len(player_guess) != 1:
            print("Invalid guess. Please enter a single letter.")
        elif not player_guess.isalpha():
            print("Invalid input. Your guess must be a letter.")
        else:
            return player_guess
        