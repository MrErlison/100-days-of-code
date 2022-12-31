from random import randint

MIN_ANSWER = 1
MAX_ANSWER = 100
EASY_LEVEL = 5
HARD_LEVEL = 10
NEUTRO_LEVEL = 7

def whatLevel():
    level = input("Choose a difficulty. Enter 'easy' or 'hard'? ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    else: # neutro
        return NEUTRO_LEVEL

def checkAnswer(playerNumber, answer, attempts):
    if playerNumber > answer:
        print("Too high.")
        attempts -= 1
    elif playerNumber < answer:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You win! The answer was {answer}.")
        attempts = -1
    
    if  attempts == 0:
        print(f"You lose. The answer was {answer}.")

    return attempts

def playGame():
    print(f"Guessing Game\nI am chose a number between {MIN_ANSWER} and {MAX_ANSWER}.")
    answer = randint(MIN_ANSWER, MAX_ANSWER)
    
    attempts = whatLevel()
    while attempts > 0:
        print(f"\nYou have {attempts} attempts.")
        playerNumber = int(input("Guess a number: "))
        attempts = checkAnswer(playerNumber, answer, attempts)

if __name__ == "__main__":
    playGame()
