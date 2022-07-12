data = input()
school = {}

while not data == 'end':
    course, student = data.split(' : ')

    if course not in school:
        school[course] = []
    school[course].append(student)

    data = input()

for course, student in sorted(school.items(), key=lambda x: (-len(x[1]))):
    print(f'{course}: {len(student)}')

    for stud in sorted(student, key=lambda x: x[0]):
        print(f"-- {stud}")
