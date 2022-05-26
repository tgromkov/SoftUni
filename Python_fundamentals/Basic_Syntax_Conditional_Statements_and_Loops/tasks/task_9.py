budget = float(input())
flour_price_per_kg = float(input())
eggs_price = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg * 1.25
milk_per_kozunak = milk_price_per_liter * 0.25
price_per_kozunak = flour_price_per_kg + eggs_price + milk_per_kozunak
current_kozunak_count = 0
coloured_eggs = 3 * current_kozunak_count

while budget > price_per_kozunak:
    budget -= price_per_kozunak
    current_kozunak_count += 1
    coloured_eggs += 3
    if current_kozunak_count % 3 == 0:
        coloured_eggs -= 2
print(f'You made {current_kozunak_count} kozunaks! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')

