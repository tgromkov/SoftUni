data = input().split(", ")
result = ''

for name in data:
    if 3 < len(name) < 16:
        if name.isalnum():
            result += name
            print(result)
