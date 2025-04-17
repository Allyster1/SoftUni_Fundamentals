repeat_string = lambda string, n: string * n

input_str = input()
counter = int(input())

result = repeat_string(input_str, counter)

print(result)