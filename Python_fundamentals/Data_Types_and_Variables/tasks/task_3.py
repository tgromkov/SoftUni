num_of_people = int(input())
capacity = int(input())
result = num_of_people / capacity

if not num_of_people % capacity == 0:
    result += 1
    print(int(result))
else:
    print(int(result))
