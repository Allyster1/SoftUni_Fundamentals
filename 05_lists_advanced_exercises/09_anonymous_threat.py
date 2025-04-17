def merge(words_list: list, merge_command: list) -> list:
    start_index, end_index = int(merge_command[1]), int(merge_command[2])

    if start_index not in range(len(words_list)):
        start_index = 0

    if end_index not in range(len(words_list)):
        end_index = len(words_list) - 1

    words_list[start_index] = "".join(words_list[start_index:end_index + 1])

    words_list = words_list[: start_index + 1] + \
                 words_list[end_index + 1:]

    return words_list


def divide(string_list: list, divide_command: list) -> str:
    index, partitions = int(divide_command[1]), int(divide_command[2])
    element = string_list[index]
    partition_size = len(element) // partitions
    partition_element = []
    number_partitions = 0

    for current_index in range(0, len(element), partition_size):
        number_partitions += 1
        if number_partitions == partitions: #last partition has to get all the symbols to the end
            current_partition = element[current_index:]
            partition_element.append(current_partition)
            break
        else:
            current_partition = element[current_index:current_index + partition_size]
            partition_element.append(current_partition)

    string_list = string_list[:index] + \
                  partition_element + \
                  string_list[index + 1:]

    return string_list


input_list = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]

    if action == "merge":
        input_list = merge(input_list, command)
    elif action == "divide":
        input_list = divide(input_list, command)

    command = input()

print(" ".join(input_list))
