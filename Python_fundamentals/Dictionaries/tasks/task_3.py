mapper = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}

while True:
    data = input().split()
    is_found = False

    for index in range(0, len(data), 2):
        quantity = int(data[index])
        item = data[index + 1].lower()

        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junk_materials:
                junk_materials[item] = quantity
            else:
                junk_materials[item] += quantity

        for key, value in key_materials.items():
            if value >= 250:
                print(f'{mapper[key]} obtained!')
                key_materials[key] -= 250
                is_found = True
                break

        if is_found:
            break

    if is_found:
        break

ordered_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))

for item, quantity in ordered_key_materials:
    print(f'{item}:{quantity}')

ordered_junk_materials = sorted(junk_materials.items(), key=lambda x: x[0])

for junk_item, junk_quantity in ordered_junk_materials:
    print(f'{junk_item}:{junk_quantity}')
