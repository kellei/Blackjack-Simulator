def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
            print(ways[j])
    return ways[amount]
 
print (changes(20, [5,10]))
