def count_coins (amount, coins):
	
	#create the array that stores all the counts
	comb = [0]*(amount+1)
	comb[0] = 1

	#for each coin in the list coins	
	for coin in coins:
			# for each count leading up to the total amount
			for count in range(coin,amount+1):
				comb[count] += comb[count - coin]
				print ("amount is {} and count is {}".format(count,comb[count]))
	return comb[amount]

amount = 12
coins = [1,2,5]
print(count_coins(amount, coins))