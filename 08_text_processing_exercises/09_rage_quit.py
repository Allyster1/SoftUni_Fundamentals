text = input()
final_text = ""
sub_string = ""
repetitions = ""

for i in range(len(text)):
    if not text[i].isdigit():
        sub_string += text[i].upper()
    else:
        for next_symbol_index in range(i, len(text)):
            if not text[next_symbol_index].isdigit():
                break
            repetitions += text[next_symbol_index]
        final_text += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""


print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)