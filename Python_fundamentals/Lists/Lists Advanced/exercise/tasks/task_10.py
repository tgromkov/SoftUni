CRITERIA = 'Craft!'
SPLITTER = ' - '
ITEM_SPLITTER = ':'

inventory = input().split(', ')
data = input()

while data != CRITERIA:
    command, item = data.split(SPLITTER)

    if command == 'Collect':
        inventory.append(item)

    elif command == 'Drop':
        if item in inventory:
            inventory.remove(item)

    elif command == 'Combine Items':
        old_item, new_item = item.split(ITEM_SPLITTER)
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(index + 1, new_item)

    elif command == 'Renew':
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    data = input()

print(', '.join(inventory))
