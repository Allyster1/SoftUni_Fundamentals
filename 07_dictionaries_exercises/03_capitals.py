country = input().split(", ")
capital = input().split(", ")
country_dict = zip(country, capital)

for country, capital in country_dict:
    print(f"{country} -> {capital}")