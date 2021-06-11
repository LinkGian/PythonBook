exchanges = ['Coinbase', 'Binance', 'FTX', 'Kraken', 'Bittrex']
message = f"My favorite exchange is {exchanges[2]}..."
message2 = f"and {exchanges[1]} is trash."
print(message)
print(message2)
exchanges.append('Bitmex') #append to add to end of list without modifying other elements of list
print(exchanges)
