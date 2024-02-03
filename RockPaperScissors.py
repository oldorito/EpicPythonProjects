import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

print("Welcome to Ola's EPIC battle of Rock, Paper, Scissors! \nYou're gonna compete against ME in this exciting game. \nIf I win, you have to buy me something off my Amazon Wishlist. \nIf you win, you will be privileged to give me a gift of your choice. \nGood luck!")
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if player >=3 or player < 0:
  print("You think you're so smart and funny, huh? You lose, checkmate!")
else:  
  print(game_images[player])
  
  computer = random.randint(0,2)
  print("My move:")
  print(game_images[computer])
  
  if player == computer:
    print("It's a draw. What a shame.")
  elif player == 0 and computer == 2:
    print("You win. I'm gonna wait for my surprise!")
  elif player == 2 and computer == 0:
    print("I win. I had my eyes on Steam Deck lately...")
  elif player > computer:
    print("You win. I'm gonna wait for my surprise!")
  elif computer > player:
    print("I win. I had my eyes on Steam Deck lately...")
  

