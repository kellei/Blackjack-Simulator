import random

class Card (object):
	def __init__(self, suit, idn, val):
		self.suit = suit
		# number used as identifier for each card
		self.id_num = idn 
		# value stores the value of the card
		self.value = val

	def show(self):
		if self.id_num == 11:
			print ("{} of {}, ID {}".format("J", self.suit, self.id_num))
		elif self.id_num == 12:
			print ("{} of {}, ID {}".format("Q", self.suit, self.id_num))	
		elif self.id_num == 13:
			print ("{} of {}, ID {}".format("K", self.suit, self.id_num))
		elif self.id_num == 1:
			print ("{} of {}, ID {}".format("A", self.suit, self.id_num))
		else:
			print ("{} of {}, ID {}".format(self.value, self.suit, self.id_num))

class Deck (object):
	def __init__(self):
		# Deck is a list of Card(s)
		self.cards = []
		self.build()

	#build cards to be added to Deck
	def build(self):
		for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for id_num in range(1,14):
				if id_num >= 10:
					value = 10
				else:
					value = id_num
				self.cards.append(Card(suit,id_num,value))

	def show(self):
		for card in self.cards:
			card.show()

	def shuffle(self):
		# verify if this is truly randomm
		# for i in range(len(self.cards)-1, 0, -1):
		# 	rand = random.randint(0, i)
		# 	self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]
		random.shuffle(self.cards)

	def draw(self):
		return self.cards.pop()

	def cards_larger(self, card_value):
		num_cards = 0
		card_larger = 0
		for card in self.cards:
			num_cards += 1 
			if card.value > card_value:
				card_larger += 1
		print (num_cards)
		return card_larger/num_cards 

deck = Deck()
deck.show()














