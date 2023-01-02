
from game_data import data
import random
import os

def selectInfluencer(choose):
    """Select influencers from data file"""
    choiceA = random.choice(data) if choose == "" else choose # keep the major
    choiceB = random.choice(data)

    while choiceA == choiceB:
        choiceB = random.choice(data)

    return choiceA, choiceB

def checkAnswer(choiceA, choiceB):
    """Return the biggest influencer"""
    if choiceA['follower_count'] > choiceB['follower_count']:
        return choiceA

    return choiceB

def playGame():
    score = 0
    choose = ""

    while True:
        os.system('clear')
        choiceA, choiceB = selectInfluencer(choose)
        print("Who has more followers?")
        print(f"A: {choiceA['name']}.\nor\nB: {choiceB['name']}.")
        choose = choiceA if input("\nType 'A' or 'B': ").strip().upper() == 'A' else choiceB
        if choose != checkAnswer(choiceA, choiceB):
            break

        score += 1

    print(f"You lose. Your score: {score}")

if __name__ == "__main__":
    playGame()
