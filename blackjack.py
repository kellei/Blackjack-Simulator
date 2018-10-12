import deck_of_cards as deck

class Player (object):
	def __init__(self, name):
		self.hand = []
		self.name = name

	def draw(self, deck):
		self.hand.append(deck.draw())

	def hand_value(self):
		val_total = 0
		for card in self.hand:
			if card.value >= 10:
				val_total += 10
			else:
				val_total += card.value
		return val_total

	def showHand (self):
		for card in self.hand:
			card.show()

# #returns the integer value of the c
# def card_value(card):

# #returns the integer value of the cards in hand
# def hand_value(hand):

#create playerss
dealer = Player("Dealer")
player_1 = Player("Player 1")

#create a deck of cards
main_deck = deck.Deck()
main_deck.shuffle()

#draw card sequence
player_1.draw(main_deck)
dealer.draw(main_deck)
player_1.draw(main_deck)
dealer.draw(main_deck)

#print outputs
print ("\n",dealer.name, "has:", dealer.hand_value())
dealer.showHand()

print ("\n",player_1.name, "has:", player_1.hand_value())
player_1.showHand()


