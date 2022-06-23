nums_input = [int(el) for el in input().split(', ')]

tens = []
twenties = []
thirties = []
forties = []
fifties = []

for el in nums_input:
    if el <= 10:
        tens.append(el)

    elif 10 < el <= 20:
        twenties.append(el)

    elif 20 < el <= 30:
        thirties.append(el)

    elif 30 < el <= 40:
        forties.append(el)

    else:
        fifties.append(el)

print(f'Group of 10\'s: {tens}')
print(f'Group of 10\'s: {twenties}')
print(f'Group of 10\'s: {thirties}')
print(f'Group of 10\'s: {forties}')
print(f'Group of 10\'s: {fifties}')
