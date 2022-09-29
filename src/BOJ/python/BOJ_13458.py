# 시험 감독

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for i in range(n):
    array[i] -= b
    if array[i] <= 0:
        answer += 1
        continue

    answer += (array[i] // c)  + 1 if array[i] % c == 0 else (array[i] // c) + 2

print(answer)
