from guess_the_number_art import logo
import random



def number_generator():
    """Generates a random number between 1 and 100"""
    return random.randint(1, 100)

def number_comparing(a,b):
    """Compares players guess with random number"""
    if a == b:
        return "Yay! you guessed the number"
    elif a > b:
        return "too high"
    elif a < b:
        return "too low"
    else:
        return "number out of range LOL"

def difficulty_mode():
    mode = (input("Choose difficulty level:\nType 'easy', 'hard' or 'mind reader'\n")).lower()
    if mode == "easy":
        return 10
    elif mode == "hard":
        return 5
    elif mode == 'mind reader':
        return 1

def game():
    print(logo)
    print("Welcome to Ola's Epic Game of Guessing!\nI'm thinking of a number 1 to 100...\n\nThere are three levels of difficulty:\nEASY - for kids and loosers. You get 10 tries.\nHARD - for players who like a challenge. You get 5 tries.\nMIND READER - for mind readers. You have only one chance.\n")
    random_number = number_generator()
    player_guess = 0
    guesses = difficulty_mode() 
    
    while player_guess != random_number:
               
        player_guess = int(input("Guess the number\n"))
        print(number_comparing(player_guess, random_number))
        guesses -= 1
        
    
        if guesses == 0:
            print(f"no more guesses, you lose, the number was {random_number}")
            return
        elif player_guess != random_number:
            print(f"you have {guesses} guesses left")
        
    
game()
    
    



