import sys
input = sys.stdin.readline

N = int(input())
answer = []
for _ in range(N):
    x, y = map(int, input().split())
    answer.append((x, y))

answer.sort(key=lambda x: (x[1], x[0]))

for item in answer:
    print(f"{item[0]} {item[1]}")