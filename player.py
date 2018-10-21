class Player (object):
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
			#add a case for A (replace it with value 21 or similar)
			if card.value >= 10:
				val_total += 10
			else:
				val_total += card.value
		return val_total

	def showHand (self):
		for card in self.hand:
			card.show()
