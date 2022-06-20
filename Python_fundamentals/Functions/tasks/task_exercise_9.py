def factorial_division(number_1, number_2):

    result_1 = 1
    result_2 = 1

    for i in range(1, number_1 + 1):
        result_1 *= i
    for k in range(1, number_2 + 1):
        result_2 *= k

    result_total = result_1 / result_2
    return result_total


number_1_input = int(input())
number_2_input = int(input())

print(f'{factorial_division(number_1_input, number_2_input):.2f}')


# different solution

def calc_factorial(n):
    res = 1
    for num in range(1, n + 1):
        res *= num
    return res


number_1 = int(input())
number_2 = int(input())

factorial_number_1 = calc_factorial(number_1)
factorial_number_2 = calc_factorial(number_2)

result = factorial_number_1 / factorial_number_2
print(f'{result:.2f}')
