gifts_input = input()
command = input()

gifts_list = gifts_input.split()

while command != 'No Money':
    event = command.split()
    if event[0] == 'OutOfStock':
        for gift in range(len(gifts_list)):
            if gifts_list[gift] == event[1]:
                gifts_list[gift] = None

    elif event[0] == 'Required':
        if int(event[2]) < len(gifts_list):
            gifts_list[int(event[2])] = event[1]

    elif event[0] == 'JustInCase':
        gifts_list[-1] = event[1]

    command = input()

print(' '.join(filter(None, gifts_list)))
