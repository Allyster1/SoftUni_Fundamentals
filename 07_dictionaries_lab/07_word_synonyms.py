words_count = int(input())
synonyms = {}

for _ in range(words_count):
    word = input()
    synonym = input()

    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonyms_list in synonyms.items():
    synonyms_str = ", ".join(synonyms_list)
    print(f"{word} - {synonyms_str}")