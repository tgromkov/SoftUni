from collections import deque

total_food = int(input())
order_quantity = [int(x) for x in input().split()]
q = deque(order_quantity)
# total_orders = 0

print(max(order_quantity))

# while len(q) > 0:
#     for el in order_quantity:
#         total_orders += q.popleft()
#
#         if total_food < total_orders:
#             print(f'Orders left: {el}')
#             break
# print("Orders complete")

is_completed = True

for _ in range(len(q)):
    order = q.popleft()

    if total_food - order < 0:
        is_completed = False
        q.appendleft(order)
        break
    total_food -= order

if is_completed:
    print("Orders complete")
else:
    q = [str(x) for x in q]
    print(f'Orders left: {" ".join(list(q))}')
