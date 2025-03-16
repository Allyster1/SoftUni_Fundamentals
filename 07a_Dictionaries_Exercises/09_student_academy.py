student_grades = {}

number_of_grades = int(input())

for _ in range(number_of_grades):
    student = input()
    current_grade = float(input())

    if student in student_grades:
        student_grades[student].append(current_grade)
    else:
        student_grades[student] = [current_grade]

filtered_students = {
    student: grades
    for student, grades in student_grades.items()
    if sum(grades) / len(grades) >= 4.50
}

for student, grades in filtered_students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {average_grade:.2f}")