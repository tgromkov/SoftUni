key = input()
value = input()
my_dict = {}

while not key == 'stop':
    value = int(value)

    if key in my_dict:
        my_dict[key] += value
    else:
        my_dict[key] = value

    key = input()
    value = input()

for key, value in my_dict.items():
    print(f'{key} -> {value}')
