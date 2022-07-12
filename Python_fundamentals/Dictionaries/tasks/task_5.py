n_rows = int(input())
data = input()
registered = {}

for n in range(n_rows):
    data_list = data.split()

    if len(data_list) == 3:
        command, user, plate = data.split()
        if command == 'register':
            if user not in registered:
                registered[user] = []
                registered[user].append(plate)
                print(f'{user} registered {plate} successfully')
            else:
                print(f"ERROR: already registered with plate number {plate}")
    else:
        command, user = data.split()
        if command == 'unregister':
            if user not in registered:
                print(f"ERROR: user {user} not found")
            elif user in registered:
                del registered[user]
                print(f'{user} unregistered successfully')

    data = input()

for user, plate in registered.items():
    print(f'{user} => {plate[0]}')
