import string

def caesar(text, shift, direction):
    alphabet = string.printable
    alphabet_lenght = len(alphabet)
    message = "" # encoded or decoded message

    shift *= -1 if direction == "decode" else 1
    
    for letter in text:
        position = alphabet.index(letter) + shift
        position %= alphabet_lenght
        message += alphabet[position]

    return message

if __name__ == "__main__":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid type!")
        exit(1)

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    message = caesar(text, shift, direction)

    if direction == "encode":
        print(f"Your cipher text is: '{message}'")
    else:
        print(f"Your plain text is: '{message}'")
