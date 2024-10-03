import random
# import art
# print(art.logo)

# initialize card deck
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
  
def initial_hands(player_score, dealer_score):
    # randomly deal card for player
    player_cards.append(random.choice(deck))
    player_cards.append(random.choice(deck))
    # randomly deal card for dealer
    dealer_cards.append(random.choice(deck))
    dealer_cards.append(random.choice(deck))

    for score in player_cards:
      player_score += score
    for score in dealer_cards:
      dealer_score += score
    # return player_score, dealer_score

def current_result():
  # show players all cards
  # show players scores
  print(f"Your cards: {player_cards}, current score: {player_score}")
  # show dealer's first card
  print(f"Computer's first card: {dealer_cards[0]}")
  
def final_result(result_message):
  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(f"{result_message}")
  
is_game_continue = "y"
result_message = "Game is not set."

while is_game_continue: 
  is_game_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  while is_game_continue == "y":
    initial_hands(player_score=player_score, dealer_score=dealer_score)
    current_result()
    # ask user input "y" for hits, "n" for stands
    is_player_hits = input("Type 'y' to get another card, type 'n' to pass: ")
    if is_player_hits == "y":
      # It's players turn
      # player get another card
      player_cards.append(random.choice(deck))
      # sum player scores
      for score in player_cards:
        player_score + score
      if player_score <= 21:
        if player_score == dealer_score:
          result_message = "It's draw."
          final_result(result_message)
        elif player_score > dealer_score: 
          result_message = "You wins!"
          final_result(result_message)
      else:
        result_message = "You lose."
        final_result(result_message)
    else:
      # It's dealer's turn
      dealer_cards.append(random.choice(deck))
      # sum dealer scores
      for score in dealer_cards:
        dealer_score + score
      if dealer_score <= 21:
        if dealer_score == dealer_score:
          result_message = "It's draw."
          final_result(result_message)
        elif dealer_score > player_score: 
          result_message = "Dealer wins!"
          final_result(result_message)
      else:
        result_message = "Player win."
        final_result(result_message)