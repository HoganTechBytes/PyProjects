'''Function to hide the secret word'''

def Hide(word: str) -> str:
    hidden_word =  ""
    for i in range(len(word)):
        if word[i] == " ":
            hidden_word += word[i]
        else:
            hidden_word += '_'
    
    return hidden_word