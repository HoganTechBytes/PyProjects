'''Function to get the secret word for Hangman'''
import random

def GetSecret():
    secret_words = ["apple", "banana", "teacher", "school", "playground", "dinosaur", "elephant", "guitar", "mountain",
           "river", "balloon", "cookie", "monkey", "soccer", "turtle", "pencil", "rainbow", "ocean", "pizza",
           "butterfly", "robot", "computer", "library", "forest", "notebook", "jacket", "giraffe", "airplane",
           "basketball", "ice cream", "treasure", "spaceship", "jungle", "volcano", "cupcake", "zebra",
           "dinosaur", "cloud", "window", "garden", "flower", "pumpkin", "starfish", "dolphin", "tiger",
           "sandwich", "island", "blanket", "clock", "hamburger"]
    
    return (random.choice(secret_words))