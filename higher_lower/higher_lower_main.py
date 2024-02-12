import random
import os
from higher_lower_art import logo, vs
from higher_lower_game_data import data


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#random account
def random_account():
    """Choose random account"""
    return random.choice(data)

def format_data(account):
    """Format data to a readable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare(guess, acc_a, acc_b):
    """Compares the guess with the follower count"""
    if acc_a > acc_b:
        return guess == "a"
    else:
        return guess == "b"
    
#print(random_account())

def game():
    
    game_on = True
    score = 0
    account_a = random_account()
    account_b = random_account()
    
    print("Weclome to Ola's EPIC and NERVE WRACKING game of Higher/Lower!\nYou will be guessing whose account has more instagram followers.\nGood luck!\n")
    print(logo)
    while game_on:
               
        account_a = account_b
        account_b = random_account()
    
        while account_a == account_b:
            account_b = random_account()
    
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B':\n ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = compare(guess, a_followers, b_followers)
    
        clear_console()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_on = False
            print(f"Ooopsie. Not this time, Champ. Final score: {score}")


game()
