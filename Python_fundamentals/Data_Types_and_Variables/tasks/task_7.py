water_tank = 255
total_water = 0
number_of_lines = int(input())

for lines in range(number_of_lines):
    new_water = int(input())
    if total_water + new_water > water_tank:
        print("Insufficient capacity!")
        continue
    else:
        total_water += new_water

print(total_water)
