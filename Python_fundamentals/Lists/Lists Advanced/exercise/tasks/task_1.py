string_input_1 = input().split(', ')
string_input_2 = input().split(', ')

result = list(set([word1 for word1 in string_input_1 for word2 in string_input_2 if word1 in word2]))

print(result)
