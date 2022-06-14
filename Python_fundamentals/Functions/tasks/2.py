def add_and_subtract(num_1, num_2, num_3):

    def sum_numbers(num1, num2):
        return num1 + num2

    def subtract_nums(num1, num2):
        return num1 - num2

    return subtract_nums(sum_numbers(num_1, num_2), num_3)


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))
