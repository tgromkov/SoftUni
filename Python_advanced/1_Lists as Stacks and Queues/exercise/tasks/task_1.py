numbers = input().split()
s = []

for n in numbers:
    s.append(int(n))

result = ''

while s:
    result += f'{s.pop()} '

print(result)
