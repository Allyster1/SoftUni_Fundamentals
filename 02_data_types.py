# 01. Concat Names
#
# first_name = input()
# last_name = input()
# delimiter = input()
#
# print(f"{first_name}{delimiter}{last_name}")
#
##################################################
# 02. Convert Meters to Kilometers
#
# meters = int(input())
#
# km = meters/1000
# print(f"{km:.2f}")
#
##################################################
# 03. Pounds to Dollars
#
# pound = int(input())
# dollars = pound * 1.31
#
# print(f"{dollars:.3f}")
#
#
#03. Pounds to Dollars with API
#
# import requests
#
# def convert_currencies(currency):
#     api_key = "53b7bb339000b9554865a0a5"
#     url = f"https://v6.exhangerate-api.com/v6/{api_key}/latest/USD"
#
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#
#         conversion_rate = data['conversion_rates']['USD']
#         usd = currency * conversion_rate
#
#         return f'{usd:.3f}'
#     else:
#         return 'Error fetching exchange rate' \
#
# currency_value = int(input())
# usd = convert_currencies(currency_value)
# print(f'{currency_value} British Pounds is equal to {usd} Dollars')
#
##################################################
# 04. Centuries to Minutes
#
# century = int(input())
# years = century * 100
# days = int(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
#
# print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
#
##################################################
# 05. Special Numbers
#
# n = int(input())
#
# for num in range(1, n+1):
#     sum = 0
#     digits = num
#
#     while digits > 0:
#         sum += digits % 10
#         digits = int(digits / 10)
#
#     if (sum == 5) or (sum == 7) or (sum == 11):
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')
#
##################################################
# 06. Next Happy Year
#
# year = int(input())
#
# while True:
#     year += 1
#     new_year = str(year)
#     set_year = set(new_year)
#
#     if len(new_year) == len(set_year):
#         break
#
#
# print(year)
