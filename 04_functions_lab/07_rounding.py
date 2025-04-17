def round_numbers(nums):
    rounded_list = []
    for n in nums:
        num = round(float(n))
        rounded_list.append(num)
    return rounded_list

input_str = input().split()
result = round_numbers(input_str)

print(result)