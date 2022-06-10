nums_input = input().split()
nums_to_remove = int(input())
nums_list = []

for el in nums_input:
    nums_list.append(int(el))
    nums_list.sort(reverse=True)

for num in range(nums_to_remove):
    nums_list.pop()

print(nums_list)
