
from game_data import data
import random
import os

def selectInfluencer():
    """Select influencers from data file"""
    choiceA = random.choice(data) 
    choiceB = random.choice(data)

    while choiceA == choiceB:
        choiceB = random.choice(data)

    return choiceA, choiceB

def checkAnswer(choiceA, choiceB):
    """Return the biggest influencer"""
    if choiceA['follower_count'] > choiceB['follower_count']:
        return 'A' 

    return 'B'

def playGame():
    score = 0

    while True:
        os.system('clear')
        choiceA, choiceB = selectInfluencer()
        print("Who has more followers?")
        print(f"A: {choiceA['name']}.\nor\nB: {choiceB['name']}.")
        choose = input("\nType 'A' or 'B': ").strip().upper()
        if choose != checkAnswer(choiceA, choiceB):
            break

        score += 1

    print(f"You lose. Your score: {score}")

if __name__ == "__main__":
    playGame()
