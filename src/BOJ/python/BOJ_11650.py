import sys
input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort()

for item in array:
    print(f"{item[0]} {item[1]}")