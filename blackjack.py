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

#initial draw sequence between platyer_1 and dealer
def draw_sequence():
	player_1.draw(main_deck)
	dealer.draw(main_deck)
	player_1.draw(main_deck)
	dealer.draw(main_deck)

def cards_on_table():
	print("===============================================")
	print ("\n",dealer.name, "has:", dealer.hand_value())
	dealer.showHand()
	print ("\n",player_1.name, "has:", player_1.hand_value())
	player_1.showHand()	

#run draw function
draw_sequence()

#print outputs
print ("\n",dealer.name, "has:", dealer.hand[0].value)
dealer.show_first()

print ("\n",player_1.name, "has:", player_1.hand_value())
player_1.showHand()

#loop runs until either player_1 
end_turn = 0
while end_turn == False:

	#request user action 
	user_action = input("\nPress H to HIT and S to STAND: ").lower()

	while user_action not in ["h","s"]:
		user_action = input("\nPress H to HIT and S to STAND: ").lower()

	#player draws card
	if user_action == "h" :
		player_1.draw(main_deck)

		#does player bust?
		if player_1.hand_value() > 21:
			end_turn = True
			print("Player 1 BUSTED!!!")
			
	#player ends turn
	else:
		end_turn == True

	#show cards present on table
	cards_on_table()











