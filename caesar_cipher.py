alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Ola's EPIC and CRYPTIC Caesar Cipher coder!\nTired of you messages being intrecepted by enemies armed forces? \nWorry no more!")

should_continue = True
def caesar(user_text, shift_amount, cipher_direction):

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in user_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_index = letter_index + shift_amount

            if new_index >= len(alphabet):
                new_index = (letter_index + shift_amount) % len(alphabet)
            if new_index <= 0:
                new_index = (letter_index - shift_amount) % len(alphabet)

            new_letter = alphabet[new_index]
            end_text += new_letter
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(user_text = text, shift_amount = shift, cipher_direction = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Byeee")



