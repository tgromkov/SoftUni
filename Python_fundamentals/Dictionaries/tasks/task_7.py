n_rows = int(input())
students = {}

for n in range(n_rows):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

sorted_students = {}

for students, grades in students.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.5:
        sorted_students[students] = average_grade

for student, av_grade in sorted(sorted_students.items(), key=lambda x: x[1], reverse=True):
    print(f'{student} -> {av_grade:.2f}')
