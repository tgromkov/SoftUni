data = input()
students = {}

while not data == 'exam finished':
    data_list = data.split('-')

    if len(data_list) == 3:
        username, language, points = data.split('-')
        points = int(points)

        if username not in students:
            students[username] = []
        if language not in students[username]:
            students[username].append(language)
        if points not in students[username]:
            students[username].append(points)

    else:
        username, command = data.split('-')

        if command == 'banned':
            del students[username]

    data = input()

print('Results:')
sorted_dict = sorted(students.items(), key=lambda x: (x[1], x[0]))
for username, points in sorted_dict:
    print(f'{username} | {points[1]}')

print('Submissions:')
for languages in sorted(students.values(), key=lambda x: x[0]):
    print(f'{languages[0]} - {len(languages)}')
