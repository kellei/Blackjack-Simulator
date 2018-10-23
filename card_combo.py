def card_combo (a,b,c=[]):
	total = sum(c)
	combo_num = 0

	if total == b:
		return 1

	elif total > b:
		#skip and do nothing
		return 0

	else:
		for i in range(len(a)):
			card_combo(a[i+1:], b, c+[a[i]])

	print(combo_num)

cards = [1,1,2]

card_combo(cards,3)