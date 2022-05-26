quantity = int(input())
days_to_christmas = int(input())
spirit = 0
total_cost = 0

for days in range(1, days_to_christmas + 1):
    if days % 11 == 0:
        quantity += 2

    if days % 2 == 0:
        total_cost += quantity * 2
        spirit += 5

    if days % 3 == 0:
        total_cost += quantity * 5 + quantity * 3
        spirit += 13

    if days % 5 == 0:
        total_cost += quantity * 15
        spirit += 17
        if days % 3 == 0:
            spirit += 30

    if days % 10 == 0:
        spirit -= 20
        total_cost += 23
        if days == days_to_christmas:
            spirit -= 30

# different solution
# if days_to_christmas % 10 == 0:
#     spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')
