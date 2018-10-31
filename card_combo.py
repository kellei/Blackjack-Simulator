'''
a is a list of available cards
b is the goal value
c is a blank list
d is a recursive variable

for every recursive loop, c stores 1 value from list a and sees
if the sum is below the goal value b

if sum of c is equal to b, return 1 (adds 1 to d)

how to add up all the match-upi scenarios between the loops
'''

def card_combo (a,b,c=[],d=0):
	total = sum(c)
	# print ("c={}".format(c))
	# print("d={}".format(d))
	# print("a={}".format(a))
	d=0

	if total == b:
		#this combo adds up to goal value
		#print ("{}".format(c))
		return 1

	if total > b:
		#skip and do nothing
		return 0

	for i in range(len(a)):
		# print("d={}".format(d))
		# print("for loop")
		d+=card_combo(a[i+1:], b, c+[a[i]], d)

	return d

# cards = [1,1,2,2,9,1,3]

# print(card_combo(cards,3))

