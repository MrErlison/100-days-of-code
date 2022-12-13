# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
rock  (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
paper     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
scissors_________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
compute_chose = random.randint(0,2)
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
#user_chose = random.randint(0,2)

if user_chose < 0 or user_chose > 2:
    print("You entered a wrong option. Game over!")
    exit(1)

print("computer" + options[compute_chose])
print("you" + options[user_chose])

if compute_chose == user_chose:
    print("It's a draw")
    exit(0)

# rock     0 win 2 scissors
# paper    1 win 0 rock
# scissors 2 win 1 paper
result = str(user_chose) + str(compute_chose)
if result == "02" or result == "10" or result == "21":
    print("You win!")
else:
    print("You lose!")
