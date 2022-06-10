HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

effort = 0
put_our_fire = []

fire_data = input().split('#')
water_amount = int(input())

for fire in fire_data:
    type_of_fire, value_of_fire = fire.split(' = ')
    value_of_fire = int(value_of_fire)

    if type_of_fire == 'High' and value_of_fire not in HIGH:
        continue
    elif type_of_fire == 'Medium' and value_of_fire not in MEDIUM:
        continue
    elif type_of_fire == 'Low' and value_of_fire not in LOW:
        continue

    if water_amount >= value_of_fire:
        water_amount -= value_of_fire
        effort += value_of_fire * 0.25
        put_our_fire.append(value_of_fire)

print('Cells:')
for value_of_fire in put_our_fire:
    print(f' - {value_of_fire}')

print(f'Effort: {effort:.2f}')
print(f'Total fire: {sum(put_our_fire)}')
