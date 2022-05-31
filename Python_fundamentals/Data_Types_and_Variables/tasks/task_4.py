number_of_lines = int(input())
character = input()
unicode_char = ord(character)
total_sum = 0

for num in range(number_of_lines + 1):
    total_sum += unicode_char

print()
print(f'The sum equals: {total_sum}')
