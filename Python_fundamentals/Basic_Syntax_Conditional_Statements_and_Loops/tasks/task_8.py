str_1 = input()
str_2 = input()
current_result = ''
previous_result = str_1

for iteration in range(len(str_1)):
    for index_str_2 in range(0, iteration + 1):
        current_result += str_2[index_str_2]

    for index_str_1 in range(iteration + 1, len(str_1)):
        current_result += str_1[index_str_1]

    if not previous_result == current_result:
        print(current_result)
    # preparing data for the next iteration
    previous_result = current_result
    current_result = ''
