import random
import os

def clear():
  """Clear screen"""
  os.system('clear')

def check_ace(cards):
  """Return the real Ace value if the score is already over 21."""
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

def calculate_score(cards):
  """Calculates the score of the cards"""
  score = sum(cards)
  
  if score == 21 and len(cards) == 2:
    return 0  
  
  check_ace(cards)
  return score

def game_result(user_cards, computer_cards):
  """Show the winner and the score"""
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

  if user_score > 21 and computer_score > 21:
    mensage = "You lose. You went over."

  if user_score == computer_score:
    mensage = "Draw."
  elif computer_score == 0:
    mensage = "You lose. Opponent has Blackjack."
  elif user_score == 0:
    mensage = "You win. Blackjack!"
  elif user_score > 21:
    mensage = "You lose. You went over."
  elif computer_score > 21:
    mensage = "You win. Opponent went over."
  elif user_score > computer_score:
    mensage = "You win."
  else:
    mensage = "You lose."
  
  print(f"\n{mensage}")

def deal_card(total_cards):
  """Return a random card from the deck"""
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cards = []

  for _ in range(total_cards):
    cards.append(random.choice(deck))

  return cards

def computer_play(cards):
  """The computer should keep drawing cards as long as it has a score less than 21"""
  while True:
    computer_score = calculate_score(cards)
    if computer_score == 0 or computer_score > 17:
      break
    cards.append(deal_card(1).pop())

  return cards

def user_play(cards):
  """User can buy cards to score"""
  while input("\nType 'y' to get another card, type 'n' to pass: ") == "y":
    cards.append(deal_card(1).pop())
    user_score = calculate_score(cards)    
    
    if user_score == 0 or user_score > 21:
      break
    
    print(f"   Your cards: {cards}, current score: {user_score}")

  return cards

def play_game():
  """Play the blackjack game"""
  user_cards = deal_card(2)
  computer_cards = deal_card(2)

  if calculate_score(computer_cards) == 0 or calculate_score(user_cards) == 0:
      game_result(user_cards, computer_cards)
      return
      
  print(f"   Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"   Computer's first card: {computer_cards[0]}")

  user_cards = user_play(user_cards)
  computer_cards = computer_play(computer_cards)

  game_result(user_cards, computer_cards)

if __name__ == "__main__":
  while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
