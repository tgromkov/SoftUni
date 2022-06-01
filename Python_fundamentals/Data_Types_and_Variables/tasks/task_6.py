number = int(input())

for _ in range(0, number):
    for __ in range(0, number):
        for ___ in range(0, number):
            print(f'{chr(97 + _)}{chr(97 + __)}{chr(97 + ___)}')


# # # different solution

# number = int(input())
# letter = ord('a')
#
# for _ in range(letter, letter + number):
#     for __ in range(letter, letter + number):
#         for ___ in range(letter, letter + number):
#             print(f'{chr(_)}{chr(__)}{chr(___)}')
