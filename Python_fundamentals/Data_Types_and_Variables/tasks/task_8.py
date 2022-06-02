number_of_companions = int(input())
days = int(input())
coins = 50 * days

for number_of_day in range(1, days + 1):
    coins -= 2 * number_of_companions

    if number_of_day % 10 == 0:
        number_of_companions -= 2

    if number_of_day % 15 == 0:
        number_of_companions += 5

    if number_of_day % 3 == 0:
        coins -= 3 * number_of_companions

    if number_of_day % 5 == 0:
        coins += number_of_companions * 20
        if number_of_day % 3 == 0:
            coins -= number_of_companions * 2

print(f"{number_of_companions} companions received {coins // number_of_companions} coins each.")
