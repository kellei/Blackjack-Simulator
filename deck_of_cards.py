import random

class Card (object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	def show(self):
		if self.value == 11:
			print ("{} of {}".format("J", self.suit))
		elif self.value == 12:
			print ("{} of {}".format("Q", self.suit))	
		elif self.value == 13:
			print ("{} of {}".format("K", self.suit))
		elif self.value == 1:
			print ("{} of {}".format("A", self.suit))
		else:
			print ("{} of {}".format(self.value, self.suit))

class Deck (object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for value in range(1,14):
				self.cards.append(Card(suit, value))

	def show(self):
		for card in self.cards:
			card.show()

	def shuffle(self):
		# verify if this is truly random
		# for i in range(len(self.cards)-1, 0, -1):
		# 	rand = random.randint(0, i)
		# 	self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()


# class Player (object):
# 	def __init__(self):
# 		self.hand = []

# 	def draw(self, deck):
# 		self.hand.append(deck.draw())

# 	def showHand (self):
# 		for card in self.hand:
# 			card.show()