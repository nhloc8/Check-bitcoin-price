import requests
import time

def get_btc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    response = requests.get(url)
    if response.status_code == 200: 
        data = response.json()
        btc_price = float(data["price"])
        return btc_price
    else:
        print("Error fetching data")
        return None

def main():
    while True:
        btc_price_usd = get_btc_price()
        if btc_price_usd is not None:
            print(f"Bitcoin price: {btc_price_usd} USD")
        else:
            print("Unable to fetch BTC price.")

        time.sleep(10)  

if __name__ == "__main__":
    main()
