from collections import defaultdict


str_input = input().replace(' ', '')
my_dict = defaultdict(int)

for char in str_input:
    my_dict[char] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')
