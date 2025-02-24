# 01. Smallest of Three Numbers
#
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
# smallest_int = min(n1,n2,n3)
# print(smallest_int)
#
##################################################
# 02. add and subtract
#
# def add_and_subtact(num1, num2, num3):
#     addition_sum = num1 + num2
#     total_sum = addition_sum - num3
#
#     return total_sum
#
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
#
# result = add_and_subtact(n1,n2,n3)
#
# print(result)
#
##################################################
# 03. Characters in Range
#
# def chars_in_range(a, b):
#
# def char_in_ascii(a,b):
#     ascii_char1 = ord(a)
#     ascii_char2 = ord(b)
#
#     ascii_data = ''
#     for i in range(ascii_char1 + 1, ascii_char2):
#         ascii_data += chr(i)
#     return " ".join(ascii_data)
#
# char1 = input()
# char2 = input()
#
# result = char_in_ascii(char1, char2)
#
# print(result)
#
#################################################
# 04. Odd and Even Sum
#
# def even_odd_sum(n):
#     even_sum = 0
#     odd_sum = 0
#
#     for num_char in str(num):
#         char = int(num_char)
#
#         if char % 2 == 0:
#             even_sum += char
#         elif char % 2 != 0:
#             odd_sum += char
#
#     res = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
#
#     return res
#
# num = int(input())
#
# result = even_odd_sum(num)
# print(result)
#
##################################################
# 05. Even Numbers
#
# def even_nums(n):
#
#     return n % 2 == 0
#
# num = input().split()
# num_list = list(map(int, num))
#
# filtered_list = list(filter(even_nums, num_list))
#
# print(filtered_list)
#
##################################################
# 06. Sort
#
# str_list = input().split()
# num_list = list(map(int, str_list))
#
# num_sorted = sorted(num_list)
#
# print(num_sorted)
#
#
##################################################
# 07. Min Max and Sum
#
# str_list = input().split()
# num_list = list(map(int, str_list))
#
# min_num = min(num_list)
# max_num = max(num_list)
# total_sum = sum(num_list)
#
# print(f"The minimum number is {min_num}")
# print(f"The maximum number is {max_num}")
# print(f"The sum number is: {total_sum}")
#
##################################################
# 08. Palindrome Integers
#
# def is_palindrome(n):
#     return n == n[::-1]
#
# str_list = input().split(", ")
#
# for s in str_list:
#     if is_palindrome(s):
#         print(True)
#     else:
#         print(False)
#
##################################################
# 09. Password Validator
#
# def validate_password(p):
#
#     is_valid = False
#
#     if n < 6 or n > 10:
#         print("Password must be between 6 and 10 characters")
#
#
#     if
# password = input()