exchanges = ['Coinbase', 'Binance', 'FTX', 'Kraken', 'Bittrex']
message = f"My favorite exchange is {exchanges[2]}..."
message2 = f"and {exchanges[1]} is trash."
print(message)
print(message2)
exchanges.append('Bitmex') #append to add to end of list without modifying other elements of list
print(exchanges)

coins = ['LINK', 'WOO', 'FTT', 'AAVE', 'BNT', 'RSR', 'DOT']
coins.sort()
print(coins)

message3 = f"If you want to make it, buy {coins[4]}"
print(message3)

for coin in coins:
    print(coin)