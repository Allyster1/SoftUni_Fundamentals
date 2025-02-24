# 01. Absolute Values
#
# numbers = input().split()
# absolute_values = []
#
# for num in numbers:
#     absolute_values.append(abs(float(num)))
#
# print(absolute_values)
#
##################################################
# 02. Grades
#
# def convert_grade(grade):
#     if 2.00 <= grade <= 2.99:
#         return "Fail"
#     elif 3.00 <= grade <= 3.49:
#         return "Poor"
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         return "Excellent"
#
# student_grade = float(input())
#
# result = convert_grade(student_grade)
# print(result)
#
##################################################
# 03. calculations
#
# def calculate_result(operation, num1, num2):
#     if operation == "multiply":
#         return num1 * num2
#     elif operation == "divide":
#         return int(num1 / num2)
#     elif operation == "add":
#         return num1 + num2
#     elif operation == "subtract":
#         return num1 - num2
#
# operator = input()
# first_number = int(input())
# second_number = int(input())
#
# result = calculate_result(operator, first_number, second_number)
# print(result)
#
##################################################
# 04. Repeat String
#
# repeat_string = lambda string, n: string * n
#
# input_str = input()
# counter = int(input())
#
# result = repeat_string(input_str, counter)
#
# print(result)
#
##################################################
# 05. Orders
#
# def calculate_price(products, counter):
#     if products == "coffee":
#        return counter * 1.50
#     elif products == "water":
#         return counter * 1.00
#     elif products == "coke":
#         return counter * 1.40
#     elif products == "snacks":
#         return counter * 2.00
#
# product = input()
# count = int(input())
#
# result = calculate_price(product, count)
#
# print(f"{result:.2f}")
#
##################################################
# 06. Calculate Rectangle Area
#
# def calculater_area(width, height):
#     return width * height
#
# num1 = int(input())
# num2 = int(input())
#
# result = calculater_area(num1, num2)
#
# print(result)
#
##################################################
# 07. Rounding
#
def round_numbers(nums):
    rounded_list = []
    for n in nums:
        num = round(float(n))
        rounded_list.append(num)
    return rounded_list

input_str = input().split()
result = round_numbers(input_str)

print(result)





##################################################
#
# helper Field

# Display all the built in functions
#import builtins
#print(dir(builtins))