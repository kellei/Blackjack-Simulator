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
		num_ace = 0
		for card in self.hand:
			if card.value >= 10:
				val_total += 10
			elif card.value == 1:
				num_ace +=1
				val_total += 11 
			else:
				val_total += card.value
		for aces in range(num_ace):
			if val_total > 21:
				val_total -= 10
		return val_total

	def showHand (self):
		for card in self.hand:
			card.show()
