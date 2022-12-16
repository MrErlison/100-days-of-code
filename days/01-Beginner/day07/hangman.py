import random
from word_list_br import word_list
from art import logo, stages

word = random.choice(word_list)
word_length = len(word)
end_of_game = False
life = 6

board = ["_" for _ in range(word_length)]

while not end_of_game:
    print(stages[life])
    print(f"{' '.join(board)}\n")
    letter = input("Digite a letra ").lower()

    if letter in board:
        print(f"Letra {letter} já informada anteriormente")

    if letter not in word:
        life -= 1
        if life == 0:
            print(stages[life])
            print(f"Você perdeu! A palavra é \"{word}\"")
            exit(1)
        continue

    for position in range(word_length):
        if letter == word[position]:
            board[position] = letter

    if "_" not in board:
        end_of_game = True
        print(f"\nParabéns, você ganhou! A palavra é \"{''.join(board)}\"")

exit(0)
