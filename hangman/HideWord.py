'''Function to hide the secret word'''

def Hide(word: str) -> str:
    hidden_word =  ""
    for letter in word:
        hidden_word += "_"
    
    return hidden_word