def my_func(number):
    divisors = []

    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)

    if sum(divisors) == number:
        return True
    return False


num_input = int(input())

if my_func(num_input):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
