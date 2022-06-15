def my_func(str1, str2):
    chars = []
    for char in range(ord(str1) + 1, ord(str2)):
        chars.append(chr(char))
    result = ' '.join(chars)
    return result


string_1 = input()
string_2 = input()

print(my_func(string_1, string_2))


########################
# using list comprehension
def my_func(str1, str2):
    chars = [chr(char) for char in range(ord(str1) + 1, ord(str2))]
    result = ' '.join(chars)
    return result


string_1 = input()
string_2 = input()

print(my_func(string_1, string_2))
