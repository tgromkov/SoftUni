from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(bul) for bul in input().split()]
locks = [int(lock) for lock in input().split()]
intelligence_value = int(input())
q = deque(locks)

