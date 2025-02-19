# 01. Strange Zoo
#
# tail = input()
# body = input()
# head = input()
#
# my_list = [tail, body, head]
#
# my_list[0], my_list[2] = my_list[2], my_list[0]
#
# print(my_list)
#
##################################################
# 02. COurses
#
# n = int(input())
#
# courses = []
#
# for _ in range(n):
#     current_course = input()
#     courses.append(current_course)
#
# print(courses)
#
##################################################
# 03. List Statistics
#
# n = int(input())
# positive_list = []
# negative_list = []
#
# for _ in range(n):
#     current_num = int(input())
#
#     if current_num >= 0:
#         positive_list.append(current_num)
#     else:
#         negative_list.append(current_num)
#
# print(positive_list)
# print(negative_list)
# print(f"Count of positives: {len(positive_list)}")
# print(f"Sum of negatives: {sum(negative_list)}")
#
##################################################
# 04. Search
#
# n = int(input())
# word = input()
#
# str_list = []
#
# for _ in range(n):
#     current_str = input()
#     str_list.append(current_str)
#
# print(str_list)
#
# for i in range(len(str_list) -1, -1, -1):
#     el = str_list[i]
#     if word not in el:
#         str_list.remove(el)
# print(str_list)
#
##################################################
# 05. Numbers Filter
#
# n = int(input())
#
# numbers_list = []
# filtered_numbers_list = []
#
# for _ in range(n):
#     current_num = int(input())
#     numbers_list.append(current_num)
#
# command = input()
#
# if command == "even":
#     for num in numbers_list:
#         if num % 2 == 0:
#             filtered_numbers_list.append(num)
# elif command == "odd":
#     for num in numbers_list:
#         if num % 2 != 0:
#             filtered_numbers_list.append(num)
# elif command == "negative":
#     for num in numbers_list:
#         if num < 0:
#             filtered_numbers_list.append(num)
# elif command == "positive":
#     for num in numbers_list:
#         if num >= 0:
#             filtered_numbers_list.append(num)
#
# print(filtered_numbers_list)