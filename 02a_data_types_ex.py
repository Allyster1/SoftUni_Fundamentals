# 1. Integer Operations
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
#
# sum = int(num1 + num2)
# division = int(sum / num3)
# multiplication = int(division * num4)
# print(multiplication)
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
# ascii_char = ""
#
#
# for i in range(first_char, last_char + 1):
#     ascii_char += chr(i) + " "
#
# print(ascii_char)
#
##################################################
# 06. Triples of Latin Letters
#
# num = int(input())
#
# for i in range(0, num):
#     for k in range(0, num):
#         for j in range(0, num):
#             print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
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
