class Dealer (object):
	def __init__(self, name):
		self.hand = []
		self.name = name
		self.bust = False

	#draws one card from the deck into the player's hand
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

	def show_first (self):
		self.hand[0].show()

	def showHand (self):
		for card in self.hand:
			card.show()
