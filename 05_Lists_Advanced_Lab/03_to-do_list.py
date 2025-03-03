def process_notes(text: str) -> list:
    todo_list = []

    while text != "End":
        todo_list.append(text)

        text = input()
    sorted_notes = sorted(todo_list, key=lambda x: int(x.split("-")[0]))
    priority_notes = [note.split("-")[1] for note in sorted_notes]

    return priority_notes


todo_note = input()

result = process_notes(todo_note)
print(result)
