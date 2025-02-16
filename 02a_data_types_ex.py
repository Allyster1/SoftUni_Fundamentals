# 1. Integer Operations
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
#
# result = (num1 + num2) // num3 * num4
#
# print(result)
#
##################################################
# 02. Chars to String
#
# char1 = input()
# char2 = input()
# char3 = input()
#
# print(char1 + char2 + char3)
#
##################################################
# 03. Elevator
#
# people = int(input())
# capacity = int(input())
#
# counter = 0
#
# for i in range(people):
#     if people > 0:
#         counter += 1
#         people -= capacity
#
# print(counter)
#
##################################################
# 04. Sum of Chars
#
# num_of_lines = int(input())
# total_sum = 0
#
# for _ in range(num_of_lines):
#     char = input()
#     total_sum += ord(char)
#
# print(f"The sum equals: {total_sum}")
#
##################################################
# 05. Print Part of the ASCII Table
#
# first_char = int(input())
# last_char = int(input())
#
# for i in range(first_char, last_char + 1):
#     if i == last_char:
#         print(chr(i))
#     else:
#         print(chr(i), end=" ")
#
#
##################################################
# 06. Triples of Latin Letters
#
# num = int(input())
#
# for i in range(97, 97 + num):
#     for k in range(97, 97 + num):
#         for j in range(97, 97 + num):
#             print(f"{chr(i)}{chr(k)}{chr(j)}")
#
##################################################
# 07. Water Overflow
#
# fillings_count = int(input())
# water_tank = 0
#
# for i in range(fillings_count):
#     liters = int(input())
#
#     if water_tank + liters > 255:
#         print("Insufficient capacity!")
#         continue
#     else:
#         water_tank += liters
#
# print(water_tank)
#
##################################################
# 08. Party Profit
#
# group_size = int(input())
# days = int(input())
# coins = 0
#
# for current_day in range(1, days + 1):
#     if current_day % 10 == 0:
#         group_size -= 2
#     if current_day % 15 == 0:
#         group_size += 5
#     if current_day % 3 == 0:
#         coins -= 3 * group_size
#     if current_day % 5 == 0:
#         coins += 20 * group_size
#         if current_day % 3 == 0:
#             coins -= 2 * group_size
#
#     coins += 50
#     coins -= 2 * group_size
#
# coins_per_person = coins // group_size
#
# print(f"{group_size} companions received {coins_per_person} coins each.")
#
##################################################
# 09. Snowballs
#
# snowballs = int(input())
# max_weight = 0
# max_time = 0
# max_value = 0
# max_quality = 0
#
# for _ in range(snowballs):
#     current_weight = int(input())
#     current_time = int(input())
#     current_quality = int(input())
#
#     current_value = int((current_weight / current_time) ** current_quality)
#
#     if current_value > max_value:
#         max_weight = current_weight
#         max_time = current_time
#         max_value = current_value
#         max_quality = current_quality
#
# print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
#
#
##################################################
# 10. Gladiator Expenses
#
# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# total_helmet_broken = lost_fights // 2
# total_sword_broken = lost_fights // 3
# total_shield_broken = lost_fights // 6
# total_armor_broken = total_sword_broken // 4
#
# expenses = total_helmet_broken * helmet_price \
#            + total_sword_broken * sword_price \
#            + total_shield_broken * shield_price \
#            + total_armor_broken * armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")