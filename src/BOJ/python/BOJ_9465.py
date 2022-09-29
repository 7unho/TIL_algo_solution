# 스티커
## 변을 공유하지 않는 스티커들의 최댓값

import sys
input = sys.stdin.readline

t = int(input())
answers = []

for _ in range(t):
    n = int(input())

    d = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        d[0][1] += d[1][0]
        d[1][1] += d[0][0]

    for i in range(2, n):
        d[0][i] += max(d[1][i - 1], d[1][i - 2])
        d[1][i] += max(d[0][i - 1], d[0][i - 2])

    answers.append(max(d[0][n - 1], d[1][n - 1]))

for answer in answers:
    print(answer)