'''Encode and decode a message using a shift cipher'''

def Encode(alphabet: list, word: str, shift: int) -> str:
    encoded_string = ""

    for letter in word:
        encoded_string += alphabet[(alphabet.index(letter) + shift)%26]

    print(encoded_string)


print("""
 
   /$$$$$$                                                           /$$$$$$  /$$           /$$                          
  /$$__  $$                                                         /$$__  $$|__/          | $$                          
 | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$       | $$  \__/ /$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
 | $$       |____  $$ /$$__  $$ /$$_____/ |____  $$ /$$__  $$      | $$      | $$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
 | $$        /$$$$$$$| $$$$$$$$|  $$$$$$   /$$$$$$$| $$  \__/      | $$      | $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
 | $$    $$ /$$__  $$| $$_____/ \____  $$ /$$__  $$| $$            | $$    $$| $$| $$  | $$| $$  | $$| $$_____/| $$      
 |  $$$$$$/|  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$            |  $$$$$$/| $$| $$$$$$$/| $$  | $$|  $$$$$$$| $$      
  \______/  \_______/ \_______/|_______/  \_______/|__/             \______/ |__/| $$____/ |__/  |__/ \_______/|__/      
                                                                                 | $$                                    
                                                                                 | $$                                    
                                                                                 |__/                                    
 
""")

alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]

word = "bunny"

Encode(alphabet, word, 15)