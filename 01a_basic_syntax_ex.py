##################################################
# 01. Jenny's Secret Message
#
# username = input()
#
# if username == "Johnny":
#     print("Hello, my love!")
# else:
#     print(f"Hello, {username}!")
#
##################################################
# 02. Drink Something
#
# age = int(input())
#
# if age <= 14:
#     print("drink toddy")
# elif age <= 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")
# elif age > 21:
#     print("drink whisky")
#
##################################################
# 03. Chat Codes
#
# n = int(input())
#
# for _ in range(n):
#     msg = int(input())
#
#     if msg == 88:
#         print("Hello")
#     elif msg == 86:
#         print("How are you?")
#     elif msg < 88:
#         print("GREAT!")
#     elif msg > 88:
#         print("Bye.")
#
##################################################
# 04. Maximum Multiple
#
# divisor = int(input())
# boundry = int(input())
# n = 0
#
# for i in range(0, boundry + 1):
#     if i / divisor > 0 and (i <= boundry and i % divisor == 0):
#         n = i
#
# print(n)
#
##################################################
# 05. Orders
#
# order_num = int(input())
# total = 0
#
# while order_num > 0:
#     price = float(input())
#     days = int(input())
#     amount = int(input())
#
#     order_num -= 1
#
#     if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= amount <= 2000:
#         print(f"The price for the coffee is: ${price * days * amount:.2f}")
#         total += price * days * amount
#     else:
#         continue
#
# print(f"Total: ${total:.2f}")
#
##################################################
# 06. String Pureness
#
# n = int(input())
#
# for _ in range(n):
#     text = input()
#
#     if "." in text or "," in text or "_" in text:
#         print(f"{text} is not pure!")
#     else:
#         print(f"{text} is pure.")
#
##################################################
# 07. Double Char
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     if command == "SoftUni":
#         continue
#
#     text = ""
#     for i in command:
#         text += i + i
#     print(text)
#
##################################################
# 08. How Much Coffee Do You Need?
#
# counter = 0
# flag = False
#
# while True:
#     command = input()
#
#     if command == "END":
#         break
#
#     text = command.lower()
#
#     if text == "dog" or text == "cat" or text == "coding" or text == "movie":
#         if command.isupper():
#             counter += 2
#         else:
#             counter += 1
#     else:
#         continue
#
#     if counter > 5:
#         print("You need extra sleep")
#         flag = True
#
# if flag is False:
#     print(counter)
#
##################################################
# 09. Sorting Hat
#
# flag = False
# while flag is False:
#     command = input()
#
#     if command == "Welcome!":
#         flag = True
#         break
#
#     if command == "Voldemort":
#         print("You must not speak of that name!")
#         break
#
#     if len(command) < 5:
#         print(f"{command} goes to Gryffindor.")
#     elif len(command) == 5:
#         print(f"{command} goes to Slytherin.")
#     elif len(command) == 6:
#         print(f"{command} goes to Ravenclaw.")
#     elif len(command) > 6:
#         print(f"{command} goes to Hufflepuff.")
#
# if flag is True:
#     print("Welcome to Hogwarts.")
##################################################
# 10. Mutate String
#
# first = input()
# second = input()
# last_printed = first
#
# for char in range(len(first)):
#     left = second[:char + 1]
#     right = first[char + 1:]
#     new_string = left + right
#
#     if new_string != last_printed:
#         print(new_string)
#         last_printed = new_string
#
##################################################
# 12. Christmas Spirit
#
# quantity = int(input())
# remaining_days = int(input())
#
# total = 0
# spirit = 0
#
# ornament_set = 2
# tree_skirt = 5
# tree_gerland = 3
# tree_lights = 15
#
# for i in range(1, remaining_days + 1):
#     if i % 11 == 0:
#         quantity += 2
#     if i % 2 == 0:
#         total += ornament_set * quantity
#         spirit += 5
#     if i % 3 == 0:
#         total += (tree_skirt + tree_gerland) * quantity
#         spirit += 13
#     if i % 5 == 0:
#         total += tree_lights * quantity
#         spirit += 17
#         if i % 3 == 0:
#             spirit += 30
#     if i % 10 == 0:
#         spirit -= 20
#         total += tree_skirt + tree_gerland + tree_lights
#
# if remaining_days % 10 == 0:
#     spirit -= 30
#
# print(f"Total cost: {total}")
# print(f"Total spirit: {spirit}")
#













