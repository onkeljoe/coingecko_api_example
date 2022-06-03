import requests
import time

Result = dict[int, str]  # define result type


# for history value take 1st entry out of 1-day-range of prices, use /market_chart/range API
def get_history_price(timestamp, coin):
    timestamp2 = timestamp + 86400  # 24 hours after timestamp1
    url = "https://api.coingecko.com/api/v3/coins/" + \
        coin + "/market_chart/range?vs_currency=usd&from=" + \
        str(timestamp) + "&to=" + str(timestamp2)

    response = requests.get(url)
    if response:
        prices = response.json()["prices"]
        ts, price = prices[0]
        return {"time": ts//1000, "price": price}
    return {}


# for current price use /simple/price API
def get_current_price(coin):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=" + \
        coin + "&vs_currencies=usd"
    response = requests.get(url).json()
    price = response[coin]["usd"]
    return {"time": round(time.time()), "price": price}


def get_price(timestamp: int, coin: str) -> Result:
    """ 
    Fetch price data for a single coin from Coingecko.

    Parameters:
    timestamp (int): The timestamp of the price in UNIX time format.
    coin (string): The Coingecko API-ID for the coin.

    Returns:
    dict {"time": int, "price": float}: timestamp of the pricefeed, price in USD.
    """
    if time.time() > timestamp:
        return get_history_price(timestamp, coin)
    return get_current_price(coin)
