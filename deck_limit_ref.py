import random
import art

# clear the screen
print("\n" * 20)
# show the logo
print(art.logo)

# Replace the deck initialization with this function
def initialize_deck(num_decks=1):
  single_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
  return single_deck * num_decks

# Add this function to draw a card from the deck
def draw_card(deck):
  if len(deck) == 0:
    return None
  return deck.pop(random.randint(0, len(deck) - 1))
  
def calculate_score(cards):
  score = 0
  for card in cards:
    score += card
  return score
  
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

# Modify the initial_hands function
def initial_hands(deck):
  player_cards = []
  dealer_cards = []
  for _ in range(2):
    player_cards.append(draw_card(deck))
    dealer_cards.append(draw_card(deck))
  return player_cards, dealer_cards

# Modify the players_turn function
def players_turn(player_cards, player_score, deck):
  global is_player_burst
  while player_score <= 21:
    is_player_hits = input("Type 'y' to get another card, type 'n' to pass: ")
    if is_player_hits == "y":
      new_card = draw_card(deck)
      if new_card is None:
        print("No more cards in the deck. Reshuffling...")
        deck.extend(initialize_deck())
        new_card = draw_card(deck)
      player_cards.append(new_card)
      # ... rest of the function remains the same ...
      # sum player scores
      player_score = calculate_score(player_cards)
      # check if Ace in hands before show current score
      if player_score > 21 and 11 in player_cards:
        # treat Ace as 1
        replace_11_with_1(player_cards)
      # show current result
      player_score = calculate_score(player_cards)
      current_result()
      if player_score > 21:
        global is_player_burst
        is_player_burst = True
        print("You burst!")
        result_message = "You lose."
        final_result(result_message)
        # global is_player_burst
        return is_player_burst
        # return is_player_burst
    elif is_player_hits == "n":
        break

# Modify the dealers_turn function
def dealers_turn(dealer_cards, dealer_score, deck):
  while dealer_score < 17:
    new_card = draw_card(deck)
    if new_card is None:
      print("No more cards in the deck. Reshuffling...")
      deck.extend(initialize_deck())
      new_card = draw_card(deck)
    dealer_cards.append(new_card)
    # ... rest of the function remains the same ...
    # sum dealer scores
    dealer_score = calculate_score(dealer_cards)
    # check if Ace in hands before show current score
    if dealer_score > 21 and 11 in dealer_cards:
      # treat Ace as 1
      replace_11_with_1(dealer_cards)
    # show current result
    dealer_score = calculate_score(dealer_cards)
    
    # check if dealer burst
    if dealer_score > 21:
      print("Dealer burst!")
      result_message = "You wins!"
      final_result(result_message)

# In the main game loop, initialize the deck and pass it to functions
is_game_continue = "y"
result_message = "Game is not set."
deck = initialize_deck(num_decks=6)  # Start with 6 decks

while is_game_continue:
  # clear the screen
  print("\n")
  is_game_continue = input("Do you want to play a game of Blackjack?\n Please Type 'y' for Yes or 'n' for No: ")
  if is_game_continue == "y":
    is_player_burst = False
    player_cards, dealer_cards = initial_hands(deck)
    # ... rest of the game logic remains the same ...
    # update both player and dealer's score based on cards get
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    current_result()
    players_turn(player_cards=player_cards, player_score=player_score, deck=deck)
    
    if is_player_burst == False:
      dealers_turn(dealer_cards=dealer_cards, dealer_score=dealer_score, deck=deck)
    
    # ... rest of the code remains the same ...

# Add this check at the end of each game round
  if len(deck) < 52:  # Reshuffle when less than one deck remains
    print("Reshuffling the deck...")
    deck = initialize_deck(num_decks=6)