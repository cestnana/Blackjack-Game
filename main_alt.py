import random
import art

# Clear the screen
print("\n" * 20)
print(art.logo)  # Show the logo

# Initialize card deck
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
  """Calculate the total score of a given list of cards."""
  score = sum(cards)
  if score > 21 and 11 in cards:
    cards[cards.index(11)] = 1  # Replace first Ace (11) with 1
    score = sum(cards)
  return score

def deal_initial_hands():
  """Deal two cards each to the player and dealer."""
  return [random.choice(deck) for _ in range(2)], [random.choice(deck) for _ in range(2)]

def show_current_result(player_cards, dealer_cards):
  """Display the current game status."""
  print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
  print(f"Computer's first card: {dealer_cards[0]}")

def show_final_result(player_cards, dealer_cards, result_message):
  """Display the final hands and the result."""
  print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
  print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
  print(result_message)

def player_turn(player_cards):
  """Manage the player's turn."""
  while calculate_score(player_cards) <= 21:
    action = input("Type 'y' to get another card, type 'n' to pass: ")
    if action == 'y':
      player_cards.append(random.choice(deck))
      show_current_result(player_cards, dealer_cards)
    else:
      break
  return calculate_score(player_cards)

def dealer_turn(dealer_cards):
  """Manage the dealer's turn."""
  while calculate_score(dealer_cards) < 17:
    dealer_cards.append(random.choice(deck))
  return calculate_score(dealer_cards)

def determine_winner(player_score, dealer_score):
  """Determine and display the result of the game."""
  if player_score > 21:
    return "You burst! You lose."
  elif dealer_score > 21:
    return "Dealer burst! You win!"
  elif player_score > dealer_score:
    return "You win!"
  elif player_score < dealer_score:
    return "You lose."
  else:
    return "It's a draw."

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  player_cards, dealer_cards = deal_initial_hands()
  show_current_result(player_cards, dealer_cards)

  player_score = player_turn(player_cards)
  if player_score <= 21:
    dealer_score = dealer_turn(dealer_cards)
  else:
    dealer_score = calculate_score(dealer_cards)  # Dealer score not needed if player bursts

  result_message = determine_winner(player_score, dealer_score)
  show_final_result(player_cards, dealer_cards, result_message)

print("Thanks for playing!")