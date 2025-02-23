# 01. Invert Values
#
# numbers_list = input().split(" ")
# inverted_list = []
#
# for current_num in numbers_list:
#     num = int(current_num)
#     if num > 0:
#         inverted_list.append(-abs(num))
#     else:
#         inverted_list.append(abs(num))
#
# print(inverted_list)
#
##################################################
# 02. Multiple List
#
# factor = int(input())
# count = int(input())
#
# num_list = []
#
# for i in range(1, count + 1):
#     i *= factor
#     num_list.append(i)
#
# print(num_list)
#
##################################################
# 03. Football Cards
#
# my_list = [f"A-{number}" for number in range(1,12)]
# my_list = [f"B-{number}" for number in range(1,12)]
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# is_terminated = False
#
# players = input().split()
#
# for player in players:
#     # if the player is found in the team, remove him
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     # if a team has less than 7 players, break
#     if len(team_a) < 7 or len(team_b) < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if is_terminated:
#     print("Game was terminated")
#
##################################################
# 04. Number Beggars
#
money_as_string = input().split(", ")
beggars_count = int(input())

money_as_integers = []

for money in money_as_string:
    money_as_integer.append(int(money))

beggars_sums = 0






##################################################
# Helper Field

# Define list
#my_list = [1,2,3,4,5]
# my_list = ['a', 'b', 'c', 'd']

# Display the index of the element in the list
# index = my_list.index("a")
# if "c" in my_list:
#     num = my_list.index("c")
#     print(num)
#     print(my_list)
# print(index)
# for i in range(2, len(my_list)):
#     print(my_list[i])

# Sorting list
# my_list.sort(reverse=True)
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list = my_list[::-1]
# print(my_list)

# Remove/Pop Element - remove(), removes the first encounter
# num = my_list.pop()
# print(my_list)
#del is same as pop, just cannot return element
# while "a" in my_list:
#     my_list.remove("a")

# Insert Element
# index = 2
# element = "apple"
# my_list.insert(index, element)
# print(my_list)

# Count of same elements in a list
# repetition = my_list.count(2)
# print(repetition)