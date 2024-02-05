import random
import art
import wordlist
#from replit import clear
import os


print(art.logo)
print(art.welcome)

chosen_word = random.choice(wordlist.wordlist)
word_lenght = len(chosen_word)
lives = 6
#print(chosen_word)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

display = []
for letter in chosen_word:
    display.append("_")

used_letters = []


game_over = False
while not game_over:
    
    guess = input("\nGuess a letter: ").lower()

    clear_console()

    if guess in display:
        #print(art.stages[lives])
        print(f"\nYou've already guessed {guess}, dummy!")
        
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            #print(art.stages[lives])
            display[position] = letter

    if guess in used_letters:
        #print(art.stages[lives])
        print(f"\nYou've already guessed {guess}, it's not there. Dumbass.")
        
    if guess not in chosen_word and guess not in used_letters:
        lives -= 1
        used_letters += guess
        #print(art.stages[lives])
        print(f"\n{guess} is not there, buddy.")
        if lives == 0:
            game_over = True
            print(f"The word was {chosen_word}.")
            print("\nYou lose ( ͡° ͜ʖ ͡°)")
            print(art.boo)

    
    print(art.stages[lives])
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        game_over = True
        print("\nYou win, I guess...")
        print(art.congrats)
