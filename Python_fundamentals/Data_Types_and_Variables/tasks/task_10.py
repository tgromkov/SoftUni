count_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

shield_breaks_counter = 0

for lost_fight in range(1, count_of_lost_fights + 1):

    if lost_fight % 2 == 0:
        expenses += helmet_price

    if lost_fight % 3 == 0:
        expenses += sword_price

    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        expenses += shield_price
        shield_breaks_counter += 1
        # different solution
        # if lost_fight % 12 == 0:
        if shield_breaks_counter % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
