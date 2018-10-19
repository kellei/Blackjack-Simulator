import deck_of_cards as deck
import player
import dealer

# #returns the integer value of the c
# def card_value(card):

# #returns the integer value of the cards in hand
# def hand_value(hand):

#create playerss
dealer = dealer.Dealer("Dealer")
player_1 = player.Player("Player 1")

#create a deck of cards
main_deck = deck.Deck()
main_deck.shuffle()

def draw_sequence():
	player_1.draw(main_deck)
	dealer.draw(main_deck)
	player_1.draw(main_deck)
	dealer.draw(main_deck)

draw_sequence()

#print outputs
print ("\n",dealer.name, "has:", dealer.hand[0].value)
dealer.show_first()

print ("\n",player_1.name, "has:", player_1.hand_value())
player_1.showHand()

user_action = input("\nPress H to HIT and S to STAND: ").lower()
print("User action is: ", user_action)

while user_action not in ["h","s"]:
	user_action = input("\nPress H to HIT and S to STAND: ").lower()

if user_action == "h" :
	print(user_action)
	player_1.draw(main_deck)
	print("===============================================")
	print ("\n",player_1.name, "has:", player_1.hand_value())
	player_1.showHand()

print("===============================================")
print ("\n",dealer.name, "has:", dealer.hand_value())
dealer.showHand()
print ("\n",player_1.name, "has:", player_1.hand_value())
player_1.showHand()	