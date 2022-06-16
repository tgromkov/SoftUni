def my_func(numbers):
    for num in numbers.split(', '):
        print(num == num[::-1])


nums_input = input()
my_func(nums_input)
