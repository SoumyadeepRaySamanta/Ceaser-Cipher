import string
from ascii_art import logo
print(logo)

alphabet = list(string.ascii_lowercase)

def cipher (direction, text, shift):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {direction}d result: {cipher_text}.")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Please give valid input.")
        direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    cipher(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    while restart not in ["yes", "no"]:
        print("Please give valid input.")
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

