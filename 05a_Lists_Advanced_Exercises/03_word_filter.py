def word_filter(word_list: list) -> str:
    filtered_words = [word for word in word_list if len(word) % 2 == 0]

    newline_words = "\n".join(filtered_words)
    return newline_words


words = input().split()

result = word_filter(words)
print(result)