rooms_count = int(input())
total_free_chairs = 0
needed_chairs_in_room = 0

for room_number in range(1, rooms_count + 1):
    chairs_count = input().split()
    chairs, people = chairs_count[0], chairs_count[1]
    chairs = int(len(chairs))
    people = int(people)

    if chairs >= people:
        total_free_chairs += chairs - people
        print(f'Game On, {total_free_chairs} free chairs left')
    else:
        needed_chairs_in_room = people - chairs
        print(f'{needed_chairs_in_room} more chairs needed in room {room_number}')
