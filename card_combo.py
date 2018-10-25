'''
a is a list of avialable cards
b is the goal value
c is a blank list

for every recursive loop, c stores 1 value from list a if the sume is below
the goal value b

how to add up all the match-upi scenarios between the loops
'''

def card_combo (a,b,c=[]):
	total = sum(c)

	if total == b:
		#this combo adds up to goal value
		print ("{}".format(c))
		return 1

	elif total > b:
		#skip and do nothing
		return 0

	else:
		for i in range(len(a)):
			return card_combo(a[i+1:], b, c+[a[i]])

cards = [1,1,1,2]

print(card_combo(cards,3))

