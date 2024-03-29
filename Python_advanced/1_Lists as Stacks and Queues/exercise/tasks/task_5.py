from collections import deque

n = int(input())
stations = deque([])

for _ in range(n):
    stations.append([el for el in input().split()])

for big_circle_iteration in range(n):
    is_valid = True
    petrol_tank = 0

    for small_circle_iteration in range(n):
        petrol_tank += int(stations[small_circle_iteration][0]) - int(stations[small_circle_iteration][1])

        if petrol_tank < 0:
            is_valid = False
            stations.append(stations.popleft())
            break

    if is_valid:
        print(big_circle_iteration)
        break
