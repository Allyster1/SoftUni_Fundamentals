char_data = input().split(", ")
data_dict = {data: ord(data) for data in char_data}

print(data_dict)
