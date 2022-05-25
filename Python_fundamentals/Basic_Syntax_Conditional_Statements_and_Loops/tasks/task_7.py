divisor = int(input())
bound = int(input())
result = 0

for num in range(bound, 0, -1):
    if num % divisor == 0:
        print(num)
        break

# another solution
if divisor > 0 and bound > 0:
    result = (bound // divisor) * divisor
    if divisor <= bound:
        if result > 0:
            print(result)
            
