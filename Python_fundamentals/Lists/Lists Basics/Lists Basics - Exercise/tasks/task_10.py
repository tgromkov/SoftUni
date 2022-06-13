energy = 100
coins = 100
daily_events = input().split('|')

for element in daily_events:
    event, number = element.split('-')
    number = int(number)

    if event == 'rest' and energy + number > 100:
        print(f'You gained 0 energy.')

    if event == 'rest' and energy + number <= 100:
        energy += number
        # print(f'Current energy: {energy}.')
        print(f'You gained {number} energy.')
        print(f'Current energy: {energy}.')

    if event == 'order' and energy >= number:
        energy -= 30
        coins += number
        print(f"You earned {number} coins.")
        if energy <= number:
            # print("You had to rest!")
            energy += 50

            # continue

    if event != 'rest' and event != 'order' and coins >= number:
        coins -= number
        print(f"You bought {event}.")
        if energy <= number:
            print("You had to rest!")
            continue
        if coins <= number:
            print(f"Closed! Cannot afford {event}.")
            break

# print(f'Current energy: {energy}.')
print("Day completed!")
print(f'Coins: {coins}')
print(f'Energy: {energy}')
