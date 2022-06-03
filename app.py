from coingecko import get_price

# Variables for the query string
timestamp1 = 1653840000
timestamp2 = 1655049600
coin = "fantom"  # CoinGecko API-ID


print(get_price(timestamp1, coin))  # history
print(get_price(timestamp2, coin))  # current
