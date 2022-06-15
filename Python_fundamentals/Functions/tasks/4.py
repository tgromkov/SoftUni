def my_function(number):
    even_sum = [int(num) for num in num_input if int(num) % 2 == 0]
    odd_sum = [int(num) for num in num_input if int(num) % 2 != 0]

    even_sum = sum(even_sum)
    odd_sum = sum(odd_sum)

    return even_sum, odd_sum


num_input = input()

even_sum_nums, odd_sum_nums = my_function(num_input)

print(f'Odd sum = {odd_sum_nums}, Even sum = {even_sum_nums}')


########################
# without list comprehension

def my_function(number):
    even_sum = []
    odd_sum = []

    for num in num_input:
        if int(num) % 2 == 0:
            even_sum.append(int(num))
        else:
            odd_sum.append(int(num))
    even_sum = sum(even_sum)
    odd_sum = sum(odd_sum)

    return even_sum, odd_sum


num_input = input()

even_sum_nums, odd_sum_nums = my_function(num_input)

print(f'Odd sum = {odd_sum_nums}, Even sum = {even_sum_nums}')
