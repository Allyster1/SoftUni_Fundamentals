##################################################
# 01. - Problem Definer
#
# num = float(input())
#
# if num == 0:
#     print("zero")
# elif num > 0:
#     if num < 1:
#         print("small positive")
#     elif num > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# else:
#     if abs(num) < 1:
#         print("small negative")
#     elif abs(num) > 1000000:
#         print("large negative")
#     else:
#         print("negative")
#
##################################################
# 02. - Largest of Three Numbers
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)
#
##################################################
# 03. Word Reverse
#
# word = input()
# rev = ""
#
# for i in range(len(word) -1, -1, -1):
#     rev += word[i]
#
# print(rev)
#
##################################################
# 04. Even Numbers
#
# n = int(input())
# flag = False
#
# for _ in range(n):
#     current = int(input())
#
#     if current % 2 != 0:
#         print(f"{current} is odd!")
#         flag = False
#         break
#     flag = True
#
# if flag == True:
#     print("All numbers are even.")
#
##################################################
#05. Number Between 1 and 100
#
# num = float(input())
#
# while not(1 <= num <= 100):
#     num = float(input())
# print(f"The number {num} is between 1 and 100")
#
##################################################
#06. Shopping
#
# budget = int(input())
# command = input()
#
# while command != "End":
#     product_price = int(command)
#     budget -= product_price
#
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     command = input()
# else:
#     print("You bought everything needed.")
##################################################
#07. Patterns
#
# pattern = int(input())
#
# for i in range(1, pattern + 1):
#     print(i * "*")
#
# for k in range(pattern - 1, -1, -1):
#     print(k * "*")