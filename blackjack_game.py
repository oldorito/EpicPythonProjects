import random
import os




def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(score1, score2):
    if score1 == score2:
        return "Draw"
    elif score2 == 0:
        return "Lose, opponent has Blackjack"
    elif score1 == 0:
        return "Win with a Blackjack"
    elif score1 > 21:
        return "You went over. You lose"
    elif score2 > 21:
        return "Opponent went over. You win"
    elif score1 > score2:
        return "You win"
    else:
        return "You lose"

def play_game():
    
    user_cards = []
    computer_cards = []

    user_score = 0
    computer_score = 0
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    
    while not game_over:  
           
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_over = True
        else:
            draw_another_card = input(("Do you want to draw another card? Type 'y' or 'n'.\n").lower())
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:                     
                game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("\nDo you want to play Blackjack? Type 'y' or 'n'.\n").lower() == "y":
    clear_console()
    play_game()


