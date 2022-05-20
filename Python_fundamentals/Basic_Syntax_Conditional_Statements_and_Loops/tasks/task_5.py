number = abs(int(input()))

for num in range(1, number + 1):
    print(f'{num} sheep...', end='')


# another solution
number = int(input())

for num in range(1, number + 1):
    if number > 0:
        print(f'{num} sheep...', end='')
