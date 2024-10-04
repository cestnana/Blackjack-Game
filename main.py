import random
import art
# clear the screen
print("\n" * 20)
# show the logo
print(art.logo)

# initialize card deck
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_cards = []
# dealer_cards = []
player_score = 0
dealer_score = 0

def calculate_score(cards):
  score = 0
  for card in cards:
    score += card
  return score
  
def initial_hands():
  # Deal cards to both player and dealer
  for _ in range(2):
    player_cards.append(random.choice(deck))
    dealer_cards.append(random.choice(deck))
    
def replace_11_with_1(hands):
  for index_of_deck in range(len(hands)):
    if hands[index_of_deck] == 11:
      hands[index_of_deck] = 1
      return hands

def current_result():
  # show players all cards and players scores
  print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
  # show dealer's first card
  print(f"Computer's first card: {dealer_cards[0]}")
  
def final_result(result_message):
  print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
  print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
  print(f"{result_message}")
  
def players_turn(player_cards, player_score, is_player_hits):
  while player_score <= 21 and is_player_hits == "y":
    # player get another card
    player_cards.append(random.choice(deck))
    # sum player scores
    player_score = calculate_score(player_cards)
    # check if Ace in hands before show current score
    if 11 in player_cards:
      # treat Ace as 1
      replace_11_with_1(player_cards)
    # show current result
    current_result()
    if player_score > 21:
      print("You burst!")
      result_message = "You lose."
      final_result(result_message)
      break
    # ask if player want to get another card
    is_player_hits = input("Type 'y' to get another card, type 'n' to pass: ")
  return is_player_hits
    
def dealers_turn(dealer_cards, dealer_score):
  while dealer_score <= 17:
    # dealer get another card
    dealer_cards.append(random.choice(deck))
    # sum dealer scores
    dealer_score = calculate_score(dealer_cards)
    # check if dealer burst
    if dealer_score > 21:
      print("Dealer burst!")
      result_message = "You wins!"
      final_result(result_message)

def determine_result():
  player_score = calculate_score(player_cards)
  dealer_score = calculate_score(dealer_cards)
  if player_score == dealer_score:
    result_message = "It's draw."
    final_result(result_message)
  elif player_score > dealer_score: 
    result_message = "You wins!"
    final_result(result_message)
  elif player_score < dealer_score:
    result_message = "You lose."
    final_result(result_message)

is_game_continue = "y"
result_message = "Game is not set."

# game main logic here
while is_game_continue: 
  # clear the screen
  print("\n")
  is_game_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if is_game_continue == "y":
    # initial first hands of both
    player_cards = []
    dealer_cards = []
    initial_hands()
    # update both player and dealer's score based on cards get
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    current_result()
    # ask user input "y" for hits, "n" for stands
    is_player_hits = input("Type 'y' to get another card, type 'n' to pass: ")
    if is_player_hits == "y":
      # It's players turn
      # players turn -> invoke function
      players_turn(player_cards=player_cards, player_score=player_score, is_player_hits=is_player_hits)
      
    # if is_player_hits == "n":
      # It's dealer's turn
      # dealer's turn -> invoke function
      dealers_turn(dealer_cards=dealer_cards, dealer_score=dealer_score)
    
    if calculate_score(player_cards) <= 21 and calculate_score(dealer_cards) <= 21:
      determine_result()
    
  else:
    break