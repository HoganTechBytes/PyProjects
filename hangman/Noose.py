'''
    Prints pictures for Hangman for a visual on lives left

        Args:
            lives (int): remaining lives of the player
        
        returns:
            NULL
'''

def Noose_Pic(lives: int):
    HANGMANPICS = ['''
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                 =========''', '''
                   +---+
                   |   |
                   O   |
                       |
                       |
                       |
                 =========''', '''
                   +---+
                   |   |
                   O   |
                   |   |
                       |
                       |
                 =========''', '''
                   +---+
                   |   |
                   O   |
                  /|   |
                       |
                       |
                 =========''', '''
                   +---+
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                 =========''', '''
                   +---+
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                 =========''', '''
                  +---+
                  |   |
                  O   |
                 /|\  |
                 / \  |
                      |
                =========''']
    
    print(HANGMANPICS[6-lives])