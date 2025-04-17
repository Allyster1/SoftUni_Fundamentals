pound = int(input())
dollars = pound * 1.31

print(f"{dollars:.3f}")


03. Pounds to Dollars with API

import requests

def convert_currencies(currency):
    api_key = "53b7bb339000b9554865a0a5"
    url = f"https://v6.exhangerate-api.com/v6/{api_key}/latest/USD"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        conversion_rate = data['conversion_rates']['USD']
        usd = currency * conversion_rate

        return f'{usd:.3f}'
    else:
        return 'Error fetching exchange rate' \

currency_value = int(input())
usd = convert_currencies(currency_value)
print(f'{currency_value} British Pounds is equal to {usd} Dollars')