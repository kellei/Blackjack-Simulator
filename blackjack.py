import deck_of_cards as deck
import player
import dealer

#create playerss
dealer = dealer.Dealer("Dealer")
player_1 = player.Player("Player 1")

#create a deck of cards
main_deck = deck.Deck()
main_deck.shuffle()

#create variables
player_turn = True
dealer_turn = True

#initial draw sequence between platyer_1 and dealer
def draw_sequence():
	#add input for more players to play
	player_1.draw(main_deck)
	dealer.draw(main_deck)
	player_1.draw(main_deck)
	dealer.draw(main_deck)

#prints the card values at play
def cards_on_table(player):
	print("===============================================")
	#dealer hand
	if player_turn == False:
		print ("\n",dealer.name, "has:", dealer.hand_value())
		dealer.showHand()
	else:
		print ("\n",dealer.name, "has:", dealer.hand[0].value)
		dealer.show_first()
	#player hand
	print ("\n",player.name, "has:", player.hand_value())
	player.showHand()

#determines the outcome of round 
def round_result(player):
	#function returns 0: tie, 1: lose, 2: win
	outcome = 0
	if 	player_turn == False and dealer_turn == False:
		if dealer.bust == False and player.bust == False:
			if dealer.hand_value() > player.hand_value():
				print ("\nPlayer LOSES")
				return 1
			elif dealer.hand_value() < player.hand_value():
				print ("\nPlayer WINS")
				return 2
			else:
				print ("Draw game")
				return 1
		elif player.bust == True:
			print ("\nPlayer LOSES")
			return 1
		else:
			print ("\nPlayer WINS")
			return 2

#displays chances of bust for player_1
def bust_percent(player):
	bust_perc = main_deck.cards_larger(21 - player.hand_value())
	print ("Bust percentage: "+"{:.0%}".format(bust_perc))

#run draw function
draw_sequence()
cards_on_table(player_1)

#loop runs until player_1 turn ends (False)
while player_turn == True:
	#display chances of bust
	bust_percent(player_1)

	#request user action 
	user_action = input("\nPress H to HIT and S to STAND: ").lower()

	while user_action not in ["h","s"]:
		user_action = input("\nPress H to HIT and S to STAND: ").lower()

	#player draws card
	if user_action == "h" :
		player_1.draw(main_deck)

		#does player bust?
		if player_1.hand_value() > 21:
			player_turn = False
			player_1.bust = True
			
	#player ends turn (s)
	else:
		player_turn = False
	#show cards present on table
	cards_on_table(player_1)

#loop runs until dealer turn ends (False)
while dealer_turn == True:

	if dealer.hand_value() < 17:
		dealer.draw(main_deck)

	elif dealer.hand_value() > 21:
		dealer.bust = True
		dealer_turn = False
		cards_on_table(player_1)

	else:
		dealer_turn = False
		cards_on_table(player_1)

round_result(player_1)








