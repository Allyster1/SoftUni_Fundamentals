def loading_bar(number: int) -> str:
    if number == 100:
        return "100% Complete! \n[%%%%%%%%%%]"
    loaded_percents = number // 10
    not_loaded_percents = 10 - loaded_percents

    return f"{number}% " \
        f"[{'%' * loaded_percents}" \
        f"{'.' * not_loaded_percents}]" \
        f"\nStill loading..."


input_number = int(input())

result = loading_bar(input_number)
print(result)
