has_ended = False
course_data = {}

while has_ended is False:
    command = input()

    if command == "end":
        has_ended = True
        break

    course, student = command.split(" : ")

    if course in course_data:
        course_data[course]["students"].append(student)
        course_data[course]["quantity"] += 1
    else:
        course_data[course] = {
            "students": [student],
            "quantity": 1
        }

for course, students_info in course_data.items():
    print(f"{course}: {students_info['quantity']}")
    for student in students_info["students"]:
        print(f"-- {student}")