has_finished = False
result_dict = {}
submissions_dict = {}

while not has_finished:
    line = input()

    if line == "exam finished":
        has_finished = True
        break

    if "-banned" in line:
        name = line.split("-")[0]
        if name in result_dict:
            del result_dict[name]
        continue

    name, language, points = line.split("-")
    points = int(points)

    if language in submissions_dict:
        submissions_dict[language] += 1
    else:
        submissions_dict[language] = 1

    if name in result_dict:
        if language in result_dict[name]:
            if result_dict[name][language] < points:
                result_dict[name][language] = points
        else:
            result_dict[name][language] = points
    else:
        result_dict[name] = {language: points}

final_results = {}
for name, languages in result_dict.items():
    total_points = sum(languages.values())
    final_results[name] = total_points

print("Results:")
for name, points in final_results.items():
    print(f"{name} | {points}")

print("Submissions:")
for language, count in submissions_dict.items():
    print(f"{language} - {count}")